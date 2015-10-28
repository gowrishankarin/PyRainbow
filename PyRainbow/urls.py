"""PyRainbow URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers
from PyRainbow.snippets import views # HOW TO MAKE THIS WORK
from PyRainbow.quickstart import views as qs_views

#from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', qs_views.UserViewSet)
router.register(r'groups', qs_views.GroupViewSet)

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^api-path/', include('rest_framework.urls', namespace='rest_framework'))
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('PyRainbow.snippets.urls')),
    url(r'^', include('customers.urls')),
    url(r'^', include('employees.urls')),
    url(r'^', include('trees.urls')) 
]
