from haystack import indexes
from .models import Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    # 全文索引[可以根据配置，可以包括多个字段索引]
    # document=True 表示当前字段为全文索引
    # use_template=True 表示接下来haystack需要加载一个固定路径的html模板文件，让text与其他索引字段绑定映射关系
    text = indexes.CharField(document=True, use_template=True)
    # 普通索引[单字段，只能提供单个字段值的搜索，所以此处的声明更主要是为了提供给上面的text全文索引使用的]
    # es索引名 = indexes.索引数据类型(model_attr="ORM中的字段名")
    id = indexes.IntegerField(model_attr="id")
    name = indexes.CharField(model_attr="name")
    description = indexes.CharField(model_attr="description")
    teacher = indexes.CharField(model_attr="teacher__name")
    course_cover = indexes.CharField(model_attr="course_cover")
    get_level_display = indexes.CharField(model_attr="get_level_display")
    students = indexes.IntegerField(model_attr="students")
    get_status_display = indexes.CharField(model_attr="get_status_display")
    lessons = indexes.IntegerField(model_attr="lessons")
    pub_lessons = indexes.IntegerField(model_attr="pub_lessons")
    price = indexes.DecimalField(model_attr="price")
    discount = indexes.CharField(model_attr="discount_json")
    orders = indexes.IntegerField(model_attr="orders")
    credit = indexes.IntegerField(model_attr="credit")

    # 指定与当前es索引模型对接的mysql的ORM模型
    def get_model(self):
        return Course

    # 当用户搜索es索引时，对应的提供的mysql数据集有哪些？
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(is_deleted=False, is_show=True)
