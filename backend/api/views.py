from urllib import request
import json
# from django.http import JsonResponse
# from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# @api_view(['GET'])
# def api_home(req, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = dict()
#     if instance:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # with model_to_dict is much easier:
#         # data = model_to_dict(instance, fields=['id', 'title', 'content', 'price'])
#         # ProductSerializer makes model_to_dict as well:
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(req, *args, **kwargs):
    serializer = ProductSerializer(data=req.data)
    # Validate if it matches the serialized Model (in serializers.py)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data) 