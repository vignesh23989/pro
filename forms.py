from django import forms
from .models import Department, Student

class BasicForm(forms.Form):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDERS)
    # We should use a validator to make sure
    # the user enters a valid number format
    phone_number = forms.CharField(label='Phone', required=False,)
    about_you = forms.CharField(widget=forms.Textarea())

class StudentForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        # fields = ['name', 'email']
        # exclude = ['name']
        model = Student


class DepartmentForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        # fields = ['name', 'email']
        # exclude = ['name']
        model = Department
