
from apps.category.models import Category
from utils import result


#  查询类目信息
def list():
    category_list = Category.objects.filter(delete_flag=0).all()
    # 实例化结果
    result = []
    # 遍历数据源
    if len(category_list) > 0:
        for item in category_list:
            # 对象
            data = item.to_dict()
            # 加入数组
            result.append(data)
    # 返回结果
    return R.ok(data=result)
