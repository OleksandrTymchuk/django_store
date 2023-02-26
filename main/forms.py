from django import forms
from django.contrib.auth.models import User


class UserSignUpForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(UserSignUpForm, self).save(commit=False)
        instance.is_superuser = False
        instance.is_staff = False
        instance.is_active = True
        if commit:
            instance.save()
        return instance

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]


class UserSignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        get_user = User.objects.filter(username__iexact=username)
        if not get_user:
            raise forms.ValidationError("Invalid user")
        return username