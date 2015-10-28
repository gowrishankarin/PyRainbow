from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trees import views

urlpatterns = [
    url(r'^trees/$', views.TreeList.as_view()),
    url(r'^trees/(?P<pk>[0-9]+)$', views.TreeDetail.as_view())
]

url = format_suffix_patterns(urlpatterns)
