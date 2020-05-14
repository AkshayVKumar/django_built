from django.urls import path
from myapp import views

app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('multi_select/',views.multi_select,name="multi_select"),
    path('form_demo/',views.form_demo,name="form_demo"),
    path('disp_form/',views.disp_form,name='disp_form'),
    path('img_demo/',views.image_ip,name="img_demo"),
    path('form_val/',views.val_form,name='form_val'),
    path('img/',views.img_mod,name="img"),
    path('images/',views.img_db,name='img_db'),
    path('register/',views.register_user,name="register"),
    path('home/',views.homepage,name="home"),
    path(r'^login/$',views.user_login,name='login'),
    path('logout/',views.user_logout,name="logout"),
    path('sample/',views.sample,name="sample"),
]
