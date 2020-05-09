from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    #manager for users
    def create_user(self,email,first_name,last_name,gender,profile_pic,dob,password):
        if not email:
            raise ValueError("Email Not Found")
        email=self.normalize_email(email)
        #create a user model
        user=self.model(email=email,first_name=first_name,last_name=last_name,\
            gender=gender,profile_pic=profile_pic,dob=dob)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,first_name,last_name,gender,profile_pic,dob,password):
        #create a super user
        user=self.create_user(email,first_name,last_name,gender,profile_pic,dob,password)
        user.is_superuser=True#assigns the super user status
        user.is_staff=True#assigns the staff status
        user.save()
        return user


choices=(('Male','Male'),('Female','Female'),('other','other'))
class UserProfile(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100,unique=True)
    gender=models.CharField(max_length=10,choices=choices,help_text="type one from [Male,Female,other]")
    dob=models.DateField(auto_now=True)
    profile_pic=models.ImageField(upload_to="profile_pics")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    #custom manager
    #name must be objects
    objects=UserProfileManager()#user defined class

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','gender',
                                'profile_pic','dob']

    def get_full_name(self):
        return self.first_name+" "+self.last_name
    
    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
# Create your models here.

class Image_upload(models.Model):
    profile_pic=models.ImageField(upload_to="%Y/%m/%d")

    
