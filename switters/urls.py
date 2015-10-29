from switters.views import SwitterViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

switter_list = SwitterViewSet.as_view({
    'get':'list',
    'post':'create'
})
switter_detail = SwitterViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})
switter_highlight = SwitterViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get':'list'
})
user_detail = UserViewSet.as_view({
    'get':'retrieve'
})

urlpatterns = [
    url(r'^$', api_root),
    url(r'^switters/$', switter_list, name='switter-list'),
    url(r'^switters/(?P<pk>[0-9]+)/$', switter_detail, name='switter-detail'),
    url(r'^switters/(?P<pk>[0-9]+)/highlight/$', switter_highlight, name='switter-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^switters/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
]


"""

from switters import views


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^switters/$', views.SwitterList.as_view(), name='switter-list'),
    url(r'^switters/(?P<pk>[0-9]+)/$', views.SwitterDetail.as_view(),
        name='switter-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^switters/(?P<pk>[0-9]+)/highlight/$', views.SwitterHighlight.as_view(),
        name='switter-highlight')
]
"""
url = format_suffix_patterns(urlpatterns)
