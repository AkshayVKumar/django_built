from django.db import models

# Create your models here.

class Image_upload(models.Model):
    profile_pic=models.ImageField(upload_to="%Y/%m/%d")

    
