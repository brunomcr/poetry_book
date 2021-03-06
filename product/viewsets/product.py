from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from product.models.product import Product
from product.serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    # Authentication
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
