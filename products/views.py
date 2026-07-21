from rest_framework.response import Response
from rest_framework import  status
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    product.delete()
    return Response({'message': 'Product deleted'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_category(request):
    serializer = CategorySerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)