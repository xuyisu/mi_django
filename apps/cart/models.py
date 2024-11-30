from django.db import models

from apps.base_model import BaseModel


# 购物车模型
class Cart(BaseModel):
    # 用户id
    user_id = models.BigIntegerField(null=True, blank=True, verbose_name='用户id')
    # 活动id
    activity_id = models.BigIntegerField(null=True, blank=True, verbose_name='活动id')
    # 活动名称
    activity_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='活动名称')
    # 商品id
    product_id = models.BigIntegerField(verbose_name='商品id')
    # 商品名称
    product_name = models.CharField(max_length=255, verbose_name='商品名称')
    # 商品简要描述
    product_subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='商品简要描述')
    # 商品图片地址
    product_main_image = models.CharField(max_length=255, null=True, blank=True, verbose_name='商品图片地址')
    # 数量
    quantity = models.PositiveIntegerField(default=0, verbose_name='数量')
    # 单价
    product_unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, verbose_name='单价')
    # 是否已选择
    selected = models.BooleanField(default=True, verbose_name='是否已选择')  # 转换为布尔值
    # 总价格
    product_total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, verbose_name='总价格')

    class Meta:
        db_table = 'cart'  # 指定数据库表名
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.product_name} - {self.quantity}x'

    def to_dict(self):
        return {
            'id': self.id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            'createUser': self.create_user,
            'updateUser': self.update_user,
            'deleteFlag': self.delete_flag,
            'userId': self.user_id,
            'activityId': self.activity_id,
            'activityName': self.activity_name,
            'productId': self.product_id,
            'productName': self.product_name,
            'productSubtitle': self.product_subtitle,
            'productMainImage': self.product_main_image,
            'quantity': self.quantity,
            'productUnitPrice': self.product_unit_price,
            'selected': self.selected,
            'productTotalPrice': self.product_total_price
        }
