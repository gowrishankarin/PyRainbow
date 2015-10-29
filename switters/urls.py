from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from switters import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^switters/$', views.SwitterList.as_view(), name='switter-list'),
    url(r'^switters/(?P<pk>[0-9]+)/$', views.SwitterDetail.as_view(),
        name='switter-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^switters/(?P<pk>[0-9]+)/hightlight/$', views.SwitterHighlight.as_view(),
        name='snippet-highlight')
]

url = format_suffix_patterns(urlpatterns)
