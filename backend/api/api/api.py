from api.models import Produit
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api.serializers import ProductSerializer

#comment developper une APIRest
@api_view(['GET', 'POST'])
def produit_api_view(request):
    if request.method == 'GET':
        products = Produit.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
