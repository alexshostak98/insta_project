from django.forms import ModelForm

from django import forms
from ..models import Profile
from django.contrib.auth.models import User


class EditProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'phone', 'bio', 'github',)


class EditUserForm(ModelForm):
    username = forms.CharField(disabled=True)
    email = forms.EmailField(disabled=True)
    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name',)

    def password_change(self):
        error = False
        new_password = self.cleaned_data['new_password']
        if new_password:
            user = self.instance
            check = user.check_password(self.cleaned_data['old_password'])
            if check and new_password == self.cleaned_data['confirm_password']:
                user.set_password(new_password)
            else:
                error = True
        return error
