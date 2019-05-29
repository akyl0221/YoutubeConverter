from django import forms


class UrlForm(forms.Form):
    url = forms.RegexField(
        regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',
        widget=forms.TextInput(attrs={'placeholder': 'Paste your Youtube link'}), max_length=300)
