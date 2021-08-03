from django import forms
from allauth.account.forms import SignupForm


class SignupUserForm(SignupForm):
    company = forms.CharField(max_length=200, label='会社名')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.company = self.cleaned_data['company']
        user.save()
        return user
