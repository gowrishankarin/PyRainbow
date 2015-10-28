from django.contrib.auth.models import User
from switters.models import Switter
from switters.serializers import SwitterSerializer
from switters.serializers import UserSerializer
from rest_framework import generics

# Create your views here.
class SwitterList(generics.ListCreateAPIView):
    queryset = Switter.objects.all()
    serializer_class = SwitterSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class SwitterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Switter.objects.all()
    serializer_class = SwitterSerializer


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
