"""test1 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^comments/', include('comments.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^app1/', include('app1.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
#   url(r'^polls/page1/', include('polls.urls')),
#   url(r'^polls/test/', include('polls.urls')),
#   url(r'^app1/page1/', include('app1.urls')),
#   url(r'^app1/page2/', include('app1.urls')),	
]
