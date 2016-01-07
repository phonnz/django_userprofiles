from django import forms

from .models import User

class CreateUserForm(forms.ModelForm):

    email = forms.EmailField()
    points = forms.CharField(widget= forms.Textarea(attrs={
    'class':'form-control',
    'placeholder':'Puntos del usuario',
    'rows':3,
    }), label='Puntos', initial='')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        ## If you just wanna render all fields from your model
        # fields = '__all__'
        ## If you wanna order and filter model fields
        fields = ('username','email', 'password', 'first_name','last_name','mom_last_name','points','avatar','certifier_document',)


class SigninUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        ## If you just wanna render all fields from your model
        # fields = '__all__'
        ## If you wanna order and filter model fields
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput(attrs= {
                'class':'regsiter-box',
                'placeholder':'Your username',
            })
        }
