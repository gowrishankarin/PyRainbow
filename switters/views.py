from django.contrib.auth.models import User
from switters.models import Switter
from switters.serializers import SwitterSerializer
from switters.serializers import UserSerializer
from switters.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route

# Create your views here.
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'switters': reverse('switter-list', request=request, format=format)
    })

class SwitterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions
    """
    queryset = Switter.objects.all()
    serializer_class = SwitterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly,)

    @detail_route(renderer_classes = [renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        switter = self.get_object()
        return Response(switter.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

"""
class SwitterHighlight(generics.GenericAPIView):
    queryset = Switter.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        switter = self.get_object()
        return Response(switter.highlighted)


class SwitterList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Switter.objects.all()
    serializer_class = SwitterSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class SwitterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly,)
    queryset = Switter.objects.all()
    serializer_class = SwitterSerializer
"""

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
"""
