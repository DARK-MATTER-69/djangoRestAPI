from api.models import Produit
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    auteur_prod = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='product_set')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','auteur_prod']
        

class ProductSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField()
    auteur =UserSerializer()
    class Meta:
        model = Produit
        fields = '__all__'
        read_only_fields = ['created_at','updated_at']

    def create(self, validated_data ):
        user = self.context['request'].user
        print('user', user)
        validated_data['auteur'] = user
        return super().create(validated_data)