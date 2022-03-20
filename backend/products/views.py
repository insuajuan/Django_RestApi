from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# Using genericViews
# https://www.django-rest-framework.org/api-guide/generic-views/

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()