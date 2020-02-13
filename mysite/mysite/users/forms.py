from django import forms
from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'email',
       ]
        widgets = {
            'password': forms.PasswordInput(),
        }


    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(user.password)
        user.save()
        return user

