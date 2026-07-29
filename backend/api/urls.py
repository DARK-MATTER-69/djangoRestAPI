from django.urls import path, include
from .views import home
from .api.api import produit_api_view 


urlpatterns = [
    path('', home, name='home'),
    path('product/', produit_api_view, name= 'product_api'),
    path('product/<int:pk>/', produit_api_view, name= 'product_api'),
    path('', include('api.api.routers')),
    
]
