"""
from trees.models import Tree
from trees.serializers import TreeSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.


class TreeList(mixins.ListModelMixin,
            mixins.CreateModelMixin,
            generics.GenericAPIView):
    """
    # List all employees, or create a new employee.
"""
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TreeDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    """
    # Retrieve, update or delete a snippet instance.
"""
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

"""
# Set of mixed-in generic views provided by rest_framework can trim down our views.py
# Below code can replace the above to work with no difference.


from trees.models import Tree
from trees.serializers import TreeSerializer
from rest_framework import generics

class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
