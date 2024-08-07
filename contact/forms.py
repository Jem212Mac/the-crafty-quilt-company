from django import forms
from .models import Contact


class ContactUs(forms.ModelForm):
    """
    Form for users to contact the site owner
    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        