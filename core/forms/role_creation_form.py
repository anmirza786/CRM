from django import forms
from core.models import Role


class RoleCreationForm(forms.Form):
    class Meta:
        model = Role
        fields = ('name', 'description')
