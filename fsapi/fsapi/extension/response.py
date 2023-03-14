from rest_framework.response import Response
from rest_framework import status


class APIResponse(Response):
    def __init__(self, code=status.HTTP_200_OK, message='OK', data=None, *args, **kwargs):
        """
        统一格式
        {
            "code": 0,
            "message": "OK",
            "data": None
        }
        """
        res_dict = {'code': code, 'message': message, 'data': data}
        res_dict.update(kwargs)
        super().__init__(data=res_dict, *args, **kwargs)
