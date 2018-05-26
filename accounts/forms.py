#from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

User = get_user_model()

class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            self.fields['username'].help_text = None
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = None
            self.helper = FormHelper()
            self.helper.form_id = ''
            self.helper.form_class = ''
            self.helper.form_method = 'post'
            self.helper.form_action = '.'
            self.helper.add_input(Submit('submit', 'Register', css_class='pull-right'))

    class Meta:
        model = User
        fields = (
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
                'country',
                'age'
            )

    def clean_country(self):
        country = self.cleaned_data.get("country")
        if country not in ['India', 'Canada']:
            raise forms.ValidationError("Sorry, registration from this country is not supported at the moment")
        return country
