from django import forms
from ckeditor.widgets import CKEditorWidget


class MailForm(forms.Form):
    mail_from = forms.EmailField(required=True)
    content = forms.CharField(widget=CKEditorWidget())
