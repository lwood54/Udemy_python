from django import forms
from newApp.models import User

class NewUserForm(forms.ModelForm):
    # if you want to do your own custom validations, add fields here:
    # first_name = forms.CharField(validator...)
    class Meta():
        model = User
        fields = '__all__'
