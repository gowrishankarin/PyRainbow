from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from customers import views


urlpatterns = [
    url(r'^customers/$', views.customer_list),
    url(r'^customers/(?P<pk>[0-9]+)$', views.customer_detail)
]

url = format_suffix_patterns(urlpatterns)
