from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customers.models import Customer
from customers.serializers import CustomerSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def customer_list(request, format = None):
    """
    List all customers, or create a new customer_list
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk, format = None):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        customer = Customer.objects.get(pk = pk)
    except Customer.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
