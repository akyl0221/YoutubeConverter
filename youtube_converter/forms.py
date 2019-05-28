from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(
        widget=forms.TextInput(attrs={'placeholder': 'Paste your Youtube link'}), max_length=300)
