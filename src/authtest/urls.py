"""authtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from log.forms import LoginForm
from log import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login),  
    url(r'^logout/$', views.logout, {'next_page': '/login'}), 
    url(r'^loggedin/$', views.loggedin, name='loggedin'), 
    url(r'^process_login/$',views.process_login,name='logout'),
    url(r'^login_error/$',views.login_error,name='login_error'),
    url(r'^register/$',views.register,name='register'),
    url(r'^complete/$',views.registration_complete ,name='complete'),

]