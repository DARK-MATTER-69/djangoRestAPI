from api.models import Produit
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

