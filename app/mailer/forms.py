from django import forms


class ComposeEmailForm(forms.Form):
    recipient = forms.EmailField(label="To")
    subject = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": 8}))