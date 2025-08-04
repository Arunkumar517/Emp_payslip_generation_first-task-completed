from django import forms
from .models import Employee
from Dashboard.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'