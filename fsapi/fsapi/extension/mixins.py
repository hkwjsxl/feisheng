from rest_framework import mixins

from response import APIResponse
from return_code import (
    VALIDATE_ERROR, AUTH_FAILED
)

class ReCreateModelMixin(mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return APIResponse(VALIDATE_ERROR, data=serializer.errors)
        res = self.perform_create(serializer)
        return res or APIResponse(data=serializer.data)


class ReListModelMixin(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return APIResponse(data=serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return APIResponse(data=serializer.data)


class ReRetrieveModelMixin(mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return APIResponse(data=serializer.data)


class ReUpdateModelMixin(mixins.UpdateModelMixin):
    def list(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return APIResponse(VALIDATE_ERROR, data=serializer.errors)
        res = self.perform_update(serializer)
        return res or APIResponse(data=serializer.data)


class ReDestroyModelMixin(mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # 验证传入的token是否跟用户token一致
        user_token = instance.user.token
        if request.auth != user_token:
            return APIResponse(AUTH_FAILED, '认证错误!')

        res = self.perform_destroy(instance)
        return res or APIResponse()
