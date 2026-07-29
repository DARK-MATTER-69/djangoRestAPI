from django.urls import path
from api.api.viewset import ProduitViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter


router = DefaultRouter()
router.register('v1/produit', ProduitViewSet, basename='product')

urlpatterns = router.urls