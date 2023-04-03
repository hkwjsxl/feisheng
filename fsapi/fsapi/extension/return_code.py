from rest_framework import status

# 成功
SUCCESS = 0

# 用户提交数据校验失败
VALIDATE_ERROR = 1001

# 认证失败
AUTH_FAILED = 1005

# 认证过期
AUTH_OVERDUE = 1006

# 无权访问
PERMISSION_DENIED = 1007

# 频率限制
TOO_MANY_REQUESTS = 1008

# 异常错误
EXCEPTION_ERROR = 1

# 服务器异常错误
SERVER_ERROR = 5000

# 创建成功
HTTP_201_CREATED = status.HTTP_201_CREATED
# 无效请求
HTTP_400_BAD_REQUEST = status.HTTP_400_BAD_REQUEST
