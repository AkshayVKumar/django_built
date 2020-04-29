from django.urls import path
from myapp import views

app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('multi_select/',views.multi_select,name="multi_select"),
    path('form_demo/',views.form_demo,name="form_demo"),
    path('disp_form/',views.disp_form,name='disp_form'),
]
