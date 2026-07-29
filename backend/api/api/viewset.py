from api.models import Produit
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.api.serializers import ProductSerializer
from rest_framework.decorators import action


class ProduitViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Produit.objects.all()
    
    @action(detail=False, methods=['GET'], url_path='expensive', url_name='ExpenProduct')
    def expensive_product(self, request, *args, **kwargs):
        products = Produit.objects.filter(price__gte=500)
        context = {'request': request}
        serializer = ProductSerializer(products, many = True,  context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)