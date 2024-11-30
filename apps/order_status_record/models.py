from django.db import models

# 订单状态记录
class OrderStatusRecord(models.Model):
    # 主键
    id = models.BigAutoField(primary_key=True, verbose_name='主键')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # 订单编号
    order_no = models.CharField(max_length=60, default='', verbose_name='订单编号')
    # 订单明细编号
    order_detail_no = models.CharField(max_length=60, default='', verbose_name='订单明细编号')
    # 商品id
    product_id = models.BigIntegerField(default=0, verbose_name='商品id')
    # 商品名称
    product_name = models.CharField(max_length=60, blank=True, null=True, verbose_name='商品名称')
    # 订单状态
    status = models.SmallIntegerField(default=0, verbose_name='订单状态')
    # 状态描述
    status_desc = models.CharField(max_length=60, blank=True, null=True, verbose_name='状态描述')

    class Meta:
        db_table = 'order_status_record'
        verbose_name = '订单记录'
        verbose_name_plural = '订单记录'

    def __str__(self):
        return f"订单编号: {self.order_no}, 订单明细编号: {self.order_detail_no}, 商品名称: {self.product_name}, 状态: {self.status_desc}"