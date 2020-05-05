from django import forms
from django.core import validators
from myapp.models import Image_upload
from django.contrib.auth.models import User



choices=(('1','Male'),('2','Female'))
#choices=((what to be carried,what to display))
class RegistrationForm(forms.Form):
    first_name=forms.CharField(max_length=20,\
                                    label="First Name : ",required=True,\
                                       validators=[validators.MinLengthValidator(3)] )
    last_name=forms.CharField(max_length=100,min_length=1,\
                    label="Last Name : ",required=True,
                    validators=[validators.MaxLengthValidator(50)])
    phno=forms.CharField(min_length=10,max_length=10,\
            label="Phone : ",required=True)
    email=forms.EmailField(min_length=5,required=True,label="Email")
    message=forms.CharField(widget=forms.Textarea,max_length=500,\
        label="Message")
    gender=forms.ChoiceField(choices=choices,widget=forms.CheckboxSelectMultiple)
    #gender=forms.ChoiceField(choices=choices)

    fav_foods=forms.ChoiceField(choices=choices,widget=forms.SelectMultiple)

class ImageForm(forms.Form):
    image=forms.ImageField(required=True)

from django.core import validators
def starts_with(name):
    if name.startswith('A'):
        return name
    raise forms.ValidationError("name is not starting with a")
import re
def check_phno(phno):
    if re.match(r'[6-9]\d{9}',phno):
        return phno
    raise forms.ValidationError('Input data is not taken')
class Sample_Form(forms.Form):
    name=forms.CharField(max_length=50,validators=[starts_with])
    email=forms.EmailField(max_length=100,\
        validators=[validators.MaxLengthValidator(100)])
    confirm_email=forms.EmailField(max_length=100)
    phone_num=forms.CharField(max_length=10,min_length=10,\
        validators=[check_phno])

    def clean_name(self):
        super(Sample_Form,self).clean()
        if len(self.cleaned_data['name'])<3:
            raise forms.ValidationError("invalid Data")
        else:
            return self.cleaned_data['name']
    def clean(self):
        super(Sample_Form,self).clean()
        if self.cleaned_data['email']!=self.cleaned_data['confirm_email']:
            raise forms.ValidationError('Email Not Matching')
        return self.cleaned_data

class ImgForm(forms.ModelForm):
    class Meta:
        model=Image_upload
        fields='__all__'

class Register_user(forms.ModelForm):
    password=forms.CharField(max_length=15,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')