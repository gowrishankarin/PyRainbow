from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from employees import views

urlpatterns = [
    url(r'^employees/$', views.EmployeeList.as_view()),
    url(r'^employees/(?P<pk>[0-9]+)$', views.EmployeeDetail.as_view())
]

url = format_suffix_patterns(urlpatterns)
