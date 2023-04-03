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

    def get(self, request):
        """获取购物车中的商品列表"""
        user_id = request.user.id
        redis = get_redis_connection("cart")
        cart_hash = redis.hgetall(f"cart_{user_id}")
        """
        cart_hash = {
            // b'商品课程ID': b'勾选状态', 
            b'2': b'1', 
            b'4': b'1', 
            b'5': b'1'
        }
        """
        if len(cart_hash) < 1:
            return APIResponse(message="购物车没有任何商品.")
        cart = [(int(key.decode()), bool(value.decode())) for key, value in cart_hash.items()]
        # cart = [ (课程id,是否勾选布尔值) (4,True) (5,True) ]
        course_id_list = [item[0] for item in cart]
        course_list = Course.objects.filter(pk__in=course_id_list, is_deleted=False, is_show=True).all()
        cart_course_data = []
        for course in course_list:
            cart_course_data.append({
                "id": course.id,
                "name": course.name,
                "course_cover": course.course_cover.url,
                "price": float(course.price),
                "discount": course.discount,
                "course_type": course.get_course_type_display(),
                # 勾选状态：把课程ID转换成bytes类型，判断当前ID是否在购物车字典中作为key存在
                # 如果存在，判断当前课程ID对应的值是否是字符串"1"，是则返回True
                "selected": (str(course.id).encode() in cart_hash) and cart_hash[
                    str(course.id).encode()].decode() == "1"
            })
        return APIResponse(data=cart_course_data)
