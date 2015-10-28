from rest_framework import serializers
from trees.models import Tree

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ('name', 'creation_time')
