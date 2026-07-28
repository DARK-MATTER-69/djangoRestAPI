from api.models import Produit
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
        read_only_fields = ['created_at','updated_at']

