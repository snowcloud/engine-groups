from django import forms
from mongoforms import MongoForm

from models import Account


class AccountForm(MongoForm):
    class Meta:
        document = Account
        fields = ('name', 'email', 'description', 'local_id')

    description = forms.CharField(widget=forms.Textarea, required=False)


# class InviteEmailToGroupForm(forms.Form):
#     emails = forms.CharField(widget=forms.Textarea())
