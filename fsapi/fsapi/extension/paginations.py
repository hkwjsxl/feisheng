from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination as DrfLimitOffsetPagination
from rest_framework.pagination import PageNumberPagination as DrfPageNumberPagination
from rest_framework.pagination import CursorPagination as DrfCursorPagination


class ReLimitOffsetPagination(DrfLimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'

    def get_paginated_response(self, data):
        return OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ])


class RePageNumberPagination(DrfPageNumberPagination):
    # 默认一页显示的条数
    page_size = 5
    # url中携带页码的key
    page_query_param = 'page'
    # url中用户携带自定义一页条数的key
    page_size_query_param = 'size'
    # 用户最大可自定义一页的条数
    max_page_size = 10

    def get_paginated_response(self, data):
        return OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ])
