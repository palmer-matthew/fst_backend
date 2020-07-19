from django import forms
from core.models import Contact
from core.models import PhoneNumber
from django.forms.models import inlineformset_factory


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ()

class PhoneNumberForm(forms.ModelForm):

    class Meta:
        model = PhoneNumber
        exclude = ()

ContactWithPhoneFormSet = inlineformset_factory(
    Contact,
    PhoneNumber,    
    form=PhoneNumberForm, 
    extra=1,
    )

