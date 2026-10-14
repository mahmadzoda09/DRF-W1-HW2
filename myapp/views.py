from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category , Product
from .serializers import CategorySerializer , ProductSerializer

@api_view(['GET' , 'POST'])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category , many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategorySerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status=400)

@api_view(['GET' , 'PATCH' , 'PUT' , 'DELETE'])
def category_detail(request,pk):
    category = Category.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = CategorySerializer(category , data = request.data)
                
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status=400)
    
    if request.method == 'PATCH':
            serializer = CategorySerializer(category , data = request.data , partial = True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors , status=400)
    
    if request.method == 'DELETE':
        category.delete()
        return Response({"Deleted Successfully"},status=204)


@api_view(['GET' , 'POST'])
def products(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product , many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status=400)


@api_view(['GET' , 'PATCH' , 'PUT' , 'DELETE'])
def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product , data = request.data)
                
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors , status=400)
    
    if request.method == 'PATCH':
            serializer = ProductSerializer(product , data = request.data , partial = True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors , status=400)
    
    if request.method == 'DELETE':
        product.delete()
        return Response({"Deleted Successfully"},status=204)