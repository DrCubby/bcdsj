from django import forms
from ticket.models import Client, Feature, Product
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ClientEditForm(forms.ModelForm):

	class Meta:
		model = Client
		fields = '__all__'

class FeatureAddForm(forms.ModelForm):
	client = forms.ModelChoiceField(queryset=Client.objects.order_by('name'))
	product = forms.ModelChoiceField(queryset=Product.objects.order_by('name'))

	class Meta:
		model = Feature
		exclude =['date_created']

class FeatureEditForm(forms.ModelForm):
	client = forms.ModelChoiceField(queryset=Client.objects.order_by('name'))
	product = forms.ModelChoiceField(queryset=Product.objects.order_by('name'))

	class Meta:
		model = Feature
		exclude =['date_created']

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductEditForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = '__all__'


class UserAddForm(forms.ModelForm):
	password = forms.CharField(label=("Password"), max_length=17, min_length=8, widget=forms.PasswordInput(attrs={'autocomplete':'off','type':'password'}))
	confirm_password = forms.CharField(label=("Password (again)"), max_length=17, min_length=8, widget=forms.PasswordInput(attrs={'autocomplete':'off','type':'password'}))

	class Meta:
		model = User
		fields = [
			'username', 'first_name', 'last_name', 'email', 'password',
			'confirm_password',
		]
		widgets = {
			'username': forms.TextInput(attrs={"autocomplete":"off",}),
		}

	def clean(self):
		"""
		Make sure the password is less than the max allowed length.
		Make sure the password and confirm_password match.
		"""
		cleaned_data = super(UserAddForm, self).clean()
		password = cleaned_data.get('password', None)
		confirm_password = cleaned_data.get('confirm_password', None)
		if password and confirm_password and (password == confirm_password):
			if int(len(password)) > 16:
				self.add_error('password', 'The password cannot exceed 16 characters.')
		else:
			self.add_error('confirm_password', 'The passwords must match.')
		return cleaned_data

	def save(self, commit=True):
		user = super(UserAddForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user

class UserEditForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
			'username', 'first_name', 'last_name','email'
		]
		widgets = {
			'username': forms.TextInput(attrs={"autocomplete":"off",}),
		}
class UserLoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
			'username', 'password'
		]
		widgets = {
			'username': forms.TextInput(attrs={"autocomplete":"off",}),
		}
