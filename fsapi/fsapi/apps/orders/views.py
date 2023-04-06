from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderModelSerializer
from mixins import ReCreateModelMixin


class OrderCreateAPIView(ReCreateModelMixin, GenericAPIView):
    """创建订单"""
    permission_classes = (IsAuthenticated,)

    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
