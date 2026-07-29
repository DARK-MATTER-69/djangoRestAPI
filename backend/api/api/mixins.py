from api.models import Produit
from api.api.serializers import ProductSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView


class ProductListView (ListModelMixin, GenericAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    
class ProductDetailView (RetrieveModelMixin, ListModelMixin, GenericAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProductSerializer
    
    def get(self, request, *args, **kwargs):
        if kwargs.get(pk):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
 
    
class ProductCreateView (CreateModelMixin, GenericAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductUpdateView (UpdateModelMixin, GenericAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
            return self.partial_update(request, *args, **kwargs)
    

class ProductDestroyView (DestroyModelMixin, GenericAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CombineApiView (ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDestroyView):
    pass