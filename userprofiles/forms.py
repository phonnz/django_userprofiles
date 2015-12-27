from django import forms

from .models import User

class CreateUserForm(forms.ModelForm):

    email = forms.EmailField()
    points = forms.CharField(widget= forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Puntos del usuario',
    'rows':4,
    }), label='Puntos')

    class Meta:
        model = User
        ## If you just wanna render all fields from your model
        # fields = '__all__'
        ## If you wanna order and filter model fields
        fields = ('username','email','first_name','last_name','mom_last_name','points','avatar','certifier_document',)
