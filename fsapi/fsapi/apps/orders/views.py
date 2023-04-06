from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderModelSerializer
from mixins import ReCreateModelMixin


class OrderCreateAPIView(ReCreateModelMixin, GenericViewSet):
    """创建订单"""
    permission_classes = (IsAuthenticated,)

    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
