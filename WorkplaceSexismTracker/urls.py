"""WorkplaceSexismTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/newEvent/$', views.newEvent, name='newEvent'),
    url('newUser', views.newUser, name='newUser'),
    url('login', views.login, name='login'),
    url(r'^(?P<user_id>[0-9]+)/eventCreated/$', views.eventCreated, name='eventCreated'),
    url('userCreated', views.userCreated, name='userCreated'),
    url('acceptLogin', views.acceptLogin, name='acceptLogin'),
]
