from django.core.exceptions import ValidationError
from django import forms

def validate_correct(value):
    if value != "r0lls0fc4sh4ndb1lls":
        raise ValidationError('%(value)s is not the right fortune', params={'value': value},)
    
class Challenge2Form(forms.Form):
    fortune = forms.CharField(validators=[validate_correct])
