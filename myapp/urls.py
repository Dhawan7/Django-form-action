from django.conf.urls import url
from myapp import views

urlpatterns = [
    url('',views.userForm,name='user_form')
]
