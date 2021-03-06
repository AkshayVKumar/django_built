from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from myapp.models import Image_upload

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome to index</h1>")

def multi_select(request):
    if request.method=="POST":
        list_select=request.POST.getlist('multi')
        list_check=request.POST.getlist('food')
        return HttpResponse(str(list_select)+"  "+str(list_check))
    return render(request,"multi_select.html")

def form_demo(request):   
    form=RegistrationForm()
    return render(request,'form_demo.html',{'form':form})

def disp_form(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print("First Name is :",form.cleaned_data['first_name'])
            print("Last Name is :",form.cleaned_data['last_name'])
            print("Phno is :",form.cleaned_data['phno'])
            print("Email is :",form.cleaned_data['email'])
            print("message is :",form.cleaned_data['message'])
    return HttpResponse(str(form.cleaned_data))


def image_ip(request):
    if request.method=="POST":
        img=request.FILES['image']
        fs=FileSystemStorage(location=settings.MEDIA_ROOT)
        file_name=fs.save(img.name,img)
        file_url=fs.url(file_name)
        return render(request,'disp_img.html',{'url_data':file_url})
    form=ImageForm()
    return render(request,'img_demo.html',{'form':form})

def val_form(request):
    if request.method=="POST":
        form=Sample_Form(request.POST)
        if form.is_valid():
            return HttpResponse(str(form.cleaned_data))
    form=Sample_Form()
    return render(request,'sam_form.html',{'form':form})

def img_mod(request):
    if request.method=="POST":
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            print("hello")
            form.save()
    form=ImgForm()
    return render(request,'sam_form.html',{'form':form})

def img_db(request):
    images=Image_upload.objects.all()
    return render(request,'img_db.html',{'images':images})

def register_user(request):
    if request.method=='POST':
        form=Register_user(request.POST,request.FILES)
        print("hello")
        if form.is_valid():
            print("hai ")
            user=form.save(commit=False)
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('myapp:home')
    form=Register_user()
    return render(request,'sam_form.html',{'form':form})

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def homepage(request):
    return render(request,"base.html")

def user_login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user:
            if user.is_active:
                login(request,user)
                print("login successful")
                return redirect('myapp:home')
            else:
                print("user is inactive")
                return redirect('myapp:home')
        else:
            return HttpResponse("Login Unsuccessful")
    return render(request,"user_login.html")

@login_required
def sample(request):
    return HttpResponse("user is logged in")

def user_logout(request):
    logout(request)
    return redirect('myapp:home')
    #return redirect('url mapping name')
    #return redirect('appname:mappingname')