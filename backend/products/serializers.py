from rest_framework import serializers

from .models import Product

# We can have multiple Serializers for the same model just in case we might need to

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]