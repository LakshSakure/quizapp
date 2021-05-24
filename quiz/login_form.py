from django import forms

# creating a form
class LoginForm(forms.Form):

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username and not password:
            raise forms.ValidationError('Please provide username and password')