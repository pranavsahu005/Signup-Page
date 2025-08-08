
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home, name='home'),
    path('front/', view.home, name='home'),
    path('signin/', view.signin, name='signin'),
    path('signup/', view.signup, name='signup'),
    path('dashboard/', view.dashboard, name='dashboard'),
]
