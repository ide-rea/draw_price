from django.core.exceptions import ValidationError
from django import forms
class user_information(forms.form):
    receiver=forms.CharField(required=True)
    tell=forms.CharField(required=True)
    address=forms.CharField(required=True)
    def clean_telephone_number(self):
        data=self.cleaned_data['telephone']
        if not data.isdigit():
            raise ValidationError('联系电话由数字组成')



