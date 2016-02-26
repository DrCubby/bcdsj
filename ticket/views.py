from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from ticket.forms import UserAddForm, UserEditForm, FeatureAddForm, FeatureEditForm, ClientAddForm, ClientEditForm
from ticket.models import Client, Feature
from django.core.urlresolvers import reverse_lazy
from braces import views
User =  get_user_model()

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

class UserDelete(DeleteView):
    """
        Delete a user
    """
    model = User
    permissions = 'auth.delete_user'
    success_url = reverse_lazy('user_list')

class UserList(ListView, views.PermissionRequiredMixin):
    """
    List of existing users.
    """
    model = User
    form_class = UserAddForm
    permissions = 'auth.change_user'
    template_name = 'ticket/user/user_list.html'

class ClientAdd(CreateView, views.PermissionRequiredMixin):
    """
        Add a client.
    """
    model = Client
    form_class = ClientAddForm
    permissions = 'ticket.add_client'
    template_name = 'ticket/client/client_add.html'
    success_url = reverse_lazy('client_list')

class ClientEdit(UpdateView):
    """
        Edit a user
    """
    model = Client
    form_class = ClientEditForm
    template_name = 'ticket/client/client_edit.html'
    success_url = reverse_lazy('client_list')

class ClientDelete(DeleteView):
    """
        Delete a user
    """
    model = Client
    permissions = 'ticket.delete_client'
    success_url = reverse_lazy('client_list')

class ClientList(ListView, views.PermissionRequiredMixin):
    """
    List of existing users.
    """
    model = Client
    form_class = ClientAddForm
    permissions = 'ticket.change_client'
    template_name = 'ticket/client/client_list.html'

class FeatureAdd(CreateView, views.PermissionRequiredMixin):
    """
        Add a client.
    """
    model = Feature
    form_class = FeatureAddForm
    permissions = 'ticket.add_feature'
    template_name = 'ticket/feature/feature_add.html'
    success_url = reverse_lazy('feature_list')

class FeatureEdit(UpdateView):
    """
        Edit a user
    """
    model = Feature
    form_class = FeatureEditForm
    template_name = 'ticket/feature/feature_edit.html'
    success_url = reverse_lazy('feature_list')

class FeatureDelete(DeleteView):
    """
        Delete a user
    """
    model = Feature
    permissions = 'ticket.delete_feature'
    success_url = reverse_lazy('feature_list')

class FeatureList(ListView, views.PermissionRequiredMixin):
    """
    List of existing users.
    """
    model = Feature
    form_class = FeatureAddForm
    permissions = 'ticket.change_feature'
    template_name = 'ticket/feature/feature_list.html'

