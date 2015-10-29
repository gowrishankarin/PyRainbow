from django.contrib.auth.models import User
from switters.models import Switter
from switters.serializers import SwitterSerializer
from switters.serializers import UserSerializer
from switters.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions

# Create your views here.
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
