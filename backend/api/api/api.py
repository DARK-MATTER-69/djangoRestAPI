from api.models import Produit
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api.serializers import ProductSerializer

#comment developper une APIRest
#       recuperer, creer, modif_complete, supp, modif 

  
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def produit_api_view(request, pk=None,*args, **kwargs):
    if request.method == 'GET':
        if pk:
            products= get_object_or_404(Produit, pk=pk)
            serializer = ProductSerializer(products)
            return Response (serializer.data, status=status.HTTP_200_OK)
        products = Produit.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'PUT':
        if pk is None :
            return Response ({'message': 'cle pk non valide'},status=status.HTTP_400_BAD_REQUEST)
        products= get_object_or_404(Produit, pk=pk)
        serializer = ProductSerializer(products,  data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    if request.method == 'DELETE':
        if pk is None :
            return Response ({'message': 'cle pk non valide'},status=status.HTTP_400_BAD_REQUEST)
        products= get_object_or_404(Produit, pk=pk)
        products.delete()
        return Response ({'message': 'suppression reussit'}, status=status.HTTP_200_OK)
    
    
    if request.method == 'PATCH':
            if pk is None :
                return Response ({'message': 'cle pk non valide'},status=status.HTTP_400_BAD_REQUEST)
            products= get_object_or_404(Produit, pk=pk)
            serializer = ProductSerializer(products,  data= request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    