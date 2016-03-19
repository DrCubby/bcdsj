from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth import authenticate, login,logout,get_user_model, logout
from django.shortcuts import render, render_to_response
from django.db.models import F, Q
from django.template import RequestContext
from django.http import HttpResponseRedirect
from ticket.forms import  SaleAddForm, SaleEditForm, ItemAddForm, ItemEditForm,  StatusAddForm, \
    StatusEditForm, UserAddForm, UserEditForm, UserLoginForm
from ticket.models import Sale, Item, Status
from django.core.urlresolvers import reverse_lazy
from braces import views
User =  get_user_model()

class SaleAdd(views.PermissionRequiredMixin, CreateView):
    """
        Add a sale.
    """
    model = Sale
    form_class = SaleAddForm
    permission_required = 'ticket.add_sale'
    template_name = 'ticket/sale/sale_add.html'
    success_url = reverse_lazy('sale_list')

class SaleEdit(UpdateView):
    """
        Edit a user
    """
    model = Sale
    form_class = SaleEditForm
    template_name = 'ticket/sale/sale_edit.html'
    success_url = reverse_lazy('sale_list')

    def get_context_data(self, **kwargs):
        context = super(SaleEdit, self).get_context_data(**kwargs)
        context['items'] = Item.objects.filter(sale_id=self.kwargs.get('pk')).order_by('sale__name','priority','date_target')
        return context

class SaleDelete(views.PermissionRequiredMixin,DeleteView):
    """
        Delete a sale
    """
    model = Sale
    permission_required = 'ticket.delete_sale'
    template_name = 'ticket/sale/sale_confirm_delete.html'
    success_url = reverse_lazy('sale_list')

class SaleList(ListView, views.PermissionRequiredMixin, views.LoginRequiredMixin):
    """
    List of existing users.
    """
    login_url = reverse_lazy('user_ass')
    redirect_field_name = 'redirect_to'
    model = Sale
    form_class = SaleAddForm
    permissions = 'ticket.change_sale'
    template_name = 'ticket/sale/sale_list.html'

    def get_queryset(self):
        return Sale.objects.all().order_by('name')

class ItemAdd(CreateView, views.PermissionRequiredMixin):
    """
        Add a sale.
    """
    model = Item
    form_class = ItemAddForm
    permissions = 'ticket.add_item'
    template_name = 'ticket/item/item_add.html'
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
        items = Item.objects.filter(sale_id = form.instance.sale_id)
        return super(ItemAdd, self).form_valid(form)

class ItemEdit(UpdateView):
    """
        Edit a user
    """
    model = Item
    form_class = ItemEditForm
    template_name = 'ticket/item/item_edit.html'
    success_url = reverse_lazy('item_list')

    #def form_valid(self, form):
     #   items = Item.objects.filter(sale_id = form.instance.sale_id).filter(priority__gte=form.instance.priority).update(priority=F('priority')+1)
      #  return super(ItemEdit, self).form_valid(form)

class ItemDelete(DeleteView):
    """
        Delete a user
    """
    model = Item
    permissions = 'ticket.delete_item'
    success_url = reverse_lazy('item_list')

class ItemList(ListView, views.PermissionRequiredMixin, ):
    """
    List of existing items.
    """
    model = Item
    form_class = ItemAddForm
    permissions = 'ticket.change_item'
    template_name = 'ticket/item/item_list.html'

class ItemSearch(views.PermissionRequiredMixin,ListView):

    model = Item
    form_class = ItemAddForm
    permission_required = 'ticket.change_item'
    template_name = 'ticket/item/item_list.html'

    def get_queryset(self):
        return Item.objects.filter(Q(title__icontains=self.request.GET['search_term'])
                                   | Q(sale__name=self.request.GET['search_term'])
                                   | Q(status__name=self.request.GET['search_term'])
                                   | Q(purchase_number__icontains=self.request.GET['search_term']))

class StatusAdd(CreateView, views.PermissionRequiredMixin):
    """
        Add a sale.
    """
    model = Status
    form_class = StatusAddForm
    permissions = 'ticket.add_status'
    template_name = 'ticket/status/status_add.html'
    success_url = reverse_lazy('status_list')

class StatusEdit(UpdateView):
    """
        Edit a user
    """
    model = Status
    form_class = StatusEditForm
    template_name = 'ticket/status/status_edit.html'
    success_url = reverse_lazy('status_list')

class StatusDelete(DeleteView):
    """
        Delete a user
    """
    model = Status
    permissions = 'ticket.delete_status'
    success_url = reverse_lazy('status_list')

class StatusList(ListView, views.PermissionRequiredMixin, views.LoginRequiredMixin):
    """
    List of existing users.
    """
    model = Status
    form_class = StatusAddForm
    permissions = 'ticket.change_status'
    template_name = 'ticket/status/status_list.html'
    login_url = reverse_lazy('user_add')

    def get_queryset(self):
        return Status.objects.all().order_by('name')

class UserAdd(CreateView, views.PermissionRequiredMixin):
    """
        Add a user.
    """
    model = User
    form_class = UserAddForm
    permissions = 'auth.add_user'
    template_name = 'ticket/user/user_add.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        """
            Save this form
        """
        form.instance.editor = self.request.user
        # Hash the password entered in the form.
        #form.instance.set_password(form.instance.password)
        form.instance.save()
        return super(UserAdd, self).form_valid(form)

class UserEdit(UpdateView):
    """
        Edit a user
    """
    model = User
    form_class = UserEditForm
    template_name = 'ticket/user/user_edit.html'
    success_url = reverse_lazy('user_list')

class UserList(ListView, views.PermissionRequiredMixin):
    """
    List of existing users.
    """
    model = User
    form_class = UserAddForm
    permissions = 'auth.change_user'
    template_name = 'ticket/user/user_list.html'

    def get_queryset(self):
        return User.objects.all().order_by('username')

def UserLogin(request):
    logout(request)
    username = password = ''
    context ={}

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'ticket/base/redirect.html')
        else:
            context['form'] = UserLoginForm()
            context['form_errors'] = 'your username and/or password does not exist'
            return render(request,'ticket/user/user_login.html', context)
    else:
        context['form'] = UserLoginForm()
        return render(request,'ticket/user/user_login.html', context)
    return render_to_response('ticket/user/user_login.html', context)

