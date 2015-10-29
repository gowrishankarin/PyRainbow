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

# Create your views here.
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'switters': reverse('switter-list', request=request, format=format)
    })

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


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
