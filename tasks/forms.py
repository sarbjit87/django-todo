from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets

User = get_user_model()

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        #self.request = kwargs.pop("request")
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        #self.fields['due_on'].widget = widgets.AdminSplitDateTime()
        #self.fields['assignee'].queryset = User.objects.filter(username__startswith="user")
