from django.urls import path
from .views import *



app_name = 'home'

urlpatterns = [
     path('send_message',handle_form,name="send_message"),
    path('',display_page,name="index")
]