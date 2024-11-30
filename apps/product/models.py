from django.db import models

# Create your models here.
from django.db import models

from apps.base_model import BaseModel


# 商品模型
class Product(BaseModel):
    # 商品id
    product_id = models.BigIntegerField(unique=True, null=True, verbose_name='商品id')
    # 品类id
    category_id = models.BigIntegerField(null=True, verbose_name='品类id')
    # 商品名称
    name = models.CharField(max_length=60, blank=True, null=True, verbose_name='商品名称')
    # 简要描述
    sub_title = models.CharField(max_length=100, blank=True, null=True, verbose_name='简要描述')
    # 商品图片地址
    main_image = models.CharField(max_length=100, blank=True, null=True, verbose_name='商品图片地址')
    # 子图片列表
    sub_images = models.CharField(max_length=100, blank=True, null=True, verbose_name='子图片列表')
    # 活动id
    activity_id = models.BigIntegerField(null=True, verbose_name='活动id')
    # 商品状态
    status = models.SmallIntegerField(default=1, verbose_name='商品状态')
    # 商品单价
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, verbose_name='商品单价')
    # 库存数
    stock = models.IntegerField(default=0, verbose_name='库存数')

    class Meta:
        db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return f"商品名称: {self.name}, 商品ID: {self.product_id}, 状态: {self.status}"

    def to_dict(self):
        return {
            'id': self.id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            'createUser': self.create_user,
            'updateUser': self.update_user,
            'productId': self.product_id,
            'categoryId': self.category_id,
            'name': self.name,
            'subTitle': self.sub_title,
            'mainImage': self.main_image,
            'subImages': self.sub_images,
            'activityId': self.activity_id,
            'status': self.status,
            'price': self.price,
            'stock': self.stock
        }
