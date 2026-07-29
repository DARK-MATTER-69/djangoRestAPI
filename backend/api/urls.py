from django.urls import path, include
from .views import home
from api.api.mixins import ProductListView, ProductDetailView, ProductUpdateView,ProductDestroyView,ProductCreateView,CombineApiView
from .api.api import produit_api_view 


urlpatterns = [
    path('', home, name='home'),
    path('product/', produit_api_view, name= 'product_api'),
    path('product/<int:pk>/', produit_api_view, name= 'product_api'),
    path('', include('api.api.routers')),
    path('v2/prodList/', ProductListView.as_view(), name='prodListview'),
    path('v2/prodDetail/<int:pk>/', ProductDetailView.as_view(), name='prodDetailview'),
    path('v2/prodCreate/<int:pk>/', ProductCreateView.as_view(), name='prodCreateview'),
    path('v2/prodUpdate/<int:pk>/', ProductUpdateView.as_view(), name='prodUpdateview'),
    path('v2/prodDestroy/', ProductDestroyView.as_view(), name='prodDestroyview'),
    path('v3/combine/', CombineApiView.as_view(), name='combine'),
    path('v3/combine/<int:pk>/', CombineApiView.as_view(), name='combine'),
    
]
