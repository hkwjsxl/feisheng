from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django_redis import get_redis_connection

from course.models import Course

from response import APIResponse
from return_code import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class CartAPIView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request):
        """添加课程商品到购物车中"""
        # 1. 接受客户端提交的商品信息：用户ID，课程ID，勾选状态
        user_id = request.user.id
        course_id = request.data.get("course_id", None)
        selected = 1  # 默认商品是勾选状态的

        # 2. 验证课程是否允许购买[is_show=True, is_deleted=False]
        # 判断课程是否存在
        is_exists = Course.objects.filter(is_show=True, is_deleted=False, pk=course_id).exists()
        if not is_exists:
            return APIResponse(HTTP_400_BAD_REQUEST, "当前课程不存在.")
        # todo 判断用户是否已经购买了

        # 3. 添加商品到购物车
        redis = get_redis_connection("cart")
        redis.hset(f"cart_{user_id}", course_id, selected)

        # 4. 获取购物车中的商品课程数量
        cart_total = redis.hlen(f"cart_{user_id}")

        # 5. 返回结果给客户端
        return APIResponse(HTTP_201_CREATED, {"msg": "成功添加商品课程到购物车.", "cart_total": cart_total})
