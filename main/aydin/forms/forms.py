from __future__ import unicode_literals, absolute_import
from django.utils.translation import gettext_lazy as _ 
from django import forms
from main.users.models import User
from main.aydin.models import Support
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator


class SupportForm(forms.ModelForm):
    class Meta : 
        model = Support
        fields = ('full_name','email','body','tel')