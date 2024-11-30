from .models import Product
from django.core.paginator import Paginator
from constants.constants import PAGE_LIMIT
from utils import result


# 商品列表
def page_list(request):
    # 页码
    page = int(request.GET.get("current", 1))
    # 每页数
    limit = int(request.GET.get("size", PAGE_LIMIT))
    # 类目id
    category_id = request.GET.get('categoryId', 0)
    # 实例化查询对象
    query = Product.objects.filter(delete_flag=False, category_id=category_id)
    # 排序
    query = query.order_by("id")
    # 设置分页
    paginator = Paginator(query, limit)
    # 记录总数
    count = paginator.count
    # 分页查询
    # 分页查询
    product_list = paginator.page(page)
    # 实例化结果
    records = []
    # 遍历数据源
    if len(product_list) > 0:
        for item in product_list:
            # 对象
            data = item.to_dict()
            # 加入数组
            records.append(data)
    result = {
        "total": count,
        "records": records,
        "current": page,
        "size": limit,
    }
    # 返回结果
    return R.ok(data=result)


# 商品详情
def get_product_detail(product_id):
    product_resp = Product.objects.filter(delete_flag=0, product_id=product_id).first()
    if not product_resp:
        return R.failed(msg="该商品已下架或删除")
    return R.ok(data=Product.to_dict(product_resp))
