from django import forms
choices=(('1','Male'),('2','Female'))
#choices=((what to be carried,what to display))
class RegistrationForm(forms.Form):
    first_name=forms.CharField(max_length=20,min_length=3,\
                                    label="First Name : ",required=True)
    last_name=forms.CharField(max_length=10,min_length=1,\
                    label="Last Name : ",required=True)
    phno=forms.CharField(min_length=10,max_length=10,\
            label="Phone : ",required=True)
    email=forms.EmailField(min_length=5,required=True,label="Email")
    message=forms.CharField(widget=forms.Textarea,max_length=500,\
        label="Message")
    gender=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
    gender=forms.ChoiceField(choices=choices)

    fav_foods=forms.ChoiceField(choices=choices,widget=forms.SelectMultiple)