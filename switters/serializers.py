from django.contrib.auth.models import User
from rest_framework import serializers
from switters.models import Switter, LANGUAGE_CHOICES, STYLE_CHOICES

class SwitterSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name = 'switter-highlight',
                            format = 'html')
    class Meta:
        model = Switter
        fields = ('url', 'title', 'code', 'linenos', 'language',
                    'style', 'owner', 'highlight')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    switters = serializers.HyperlinkedRelatedField(many = True,
        view_name = 'switter-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'switters')
