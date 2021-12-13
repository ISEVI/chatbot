from django import forms


class UserForm(forms.Form):
    question = forms.CharField(max_length=100)
