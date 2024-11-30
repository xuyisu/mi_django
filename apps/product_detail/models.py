from django.db import models
from django.db.models import JSONField  # 确保你的Django版本支持JSONField

from apps.base_model import BaseModel


class ProductDetail(BaseModel):
    # 商品id
    product_id = models.BigIntegerField(verbose_name='商品id')
    # 商品详情
    detail = JSONField(null=True, verbose_name='商品详情', blank=True)
    # 商品参数
    param = JSONField(null=True, verbose_name='商品参数', blank=True)
    # 轮播图片
    rotation = JSONField(null=True, verbose_name='轮播图片', blank=True)

    class Meta:
        db_table = 'product_detail'
        verbose_name = '商品明细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"商品ID: {self.product_id}, 创建时间: {self.create_time}"