
from django.contrib import admin
from django.urls import path
from django.conf import settings
from . view import *
from loginproject import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home, name='home'),
    path('front/',view.home, name='home'),
    path('signin/',view.signin, name='signin'),
    path('signup/',view.signup, name='signup'),
]




