from django.contrib.auth.models import User
from rest_framework import serializers
from switters.models import Switter, LANGUAGE_CHOICES, STYLE_CHOICES

class SwitterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Switter
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.ModelSerializer):
    switters = serializers.PrimaryKeyRelatedField(many = True, queryset = Switter.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
