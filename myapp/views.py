from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import *
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