from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="نام")
    email = forms.EmailField(label="ایمیل")
    message = forms.CharField(label="پیام", widget=forms.Textarea)
