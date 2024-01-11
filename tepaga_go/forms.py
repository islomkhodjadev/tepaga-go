from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.OrderPlace
        fields = ['name', 'phone', 'content']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ism'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Telefon raqam'})
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 9, 'placeholder': 'Matn'})
