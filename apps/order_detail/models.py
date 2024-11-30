from django.db import models

from apps.base_model import BaseModel
from decimal import Decimal

# 订单明细模型
class OrderDetail(BaseModel):
    # 订单编号
    order_no = models.CharField(max_length=60, default='', verbose_name='订单编号')
    # 订单明细编号
    order_detail_no = models.CharField(max_length=60, default='', verbose_name='订单明细编号')
    # 活动id
    activity_id = models.BigIntegerField(default=0, null=True, blank=True, verbose_name='活动id')
    # 活动名称
    activity_name = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name='活动名称')
    # 活动图片地址
    activity_main_image = models.CharField(max_length=100, default='', null=True, blank=True,verbose_name='活动图片地址')
    # 商品id
    product_id = models.BigIntegerField(default=0, verbose_name='商品id')
    # 商品名称
    product_name = models.CharField(max_length=50, default='', verbose_name='商品名称')
    # 商品图片地址
    product_main_image = models.CharField(max_length=100, default='', verbose_name='商品图片地址')
    # 单价
    current_unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'), null=True, blank=True, verbose_name='单价')
    # 数量
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='数量')
    # 总价
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'), null=True, blank=True, verbose_name='总价')
    # 购买人id
    user_id = models.BigIntegerField(default=0, verbose_name='购买人id')
    # 订单状态
    status = models.SmallIntegerField(default=0, verbose_name='订单状态')
    # 状态描述
    status_desc = models.CharField(max_length=20, default='', null=True, blank=True, verbose_name='状态描述')
    # 取消时间
    cancel_time = models.DateTimeField(null=True, blank=True, verbose_name='取消时间')
    # 取消原因
    cancel_reason = models.IntegerField(default=0, null=True, blank=True, verbose_name='取消原因')
    # 发货时间
    send_time = models.DateTimeField(null=True, blank=True, verbose_name='发货时间')
    # 签收时间
    receive_time = models.DateTimeField(null=True, blank=True, verbose_name='签收时间')

    class Meta:
        db_table = 'order_detail'
        verbose_name = '订单明细'
        verbose_name_plural = '订单明细'

    def __str__(self):
        return f"订单明细编号: {self.order_detail_no}"

    def to_dict(self):
        """
        将模型实例转换为驼峰命名风格的字典
        """
        return {
            'id': self.id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            'createUser': self.create_user,
            'updateUser': self.update_user,
            'orderNo': self.order_no,
            'orderDetailNo': self.order_detail_no,
            'activityId': self.activity_id,
            'activityName': self.activity_name,
            'activityMainImage': self.activity_main_image,
            'productId': self.product_id,
            'productName': self.product_name,
            'productMainImage': self.product_main_image,
            'currentUnitPrice': self.current_unit_price,
            'quantity': self.quantity,
            'totalPrice': self.total_price,
            'userId': self.user_id,
            'status': self.status,
            'statusDesc': self.status_desc,
            'cancelTime': str(self.cancel_time.strftime('%Y-%m-%d %H:%M:%S')) if self.cancel_time else None,
            'cancelReason': self.cancel_reason,
            'sendTime': self.send_time.isoformat() if self.send_time else None,
            'receiveTime': str(self.receive_time.strftime('%Y-%m-%d %H:%M:%S')) if self.receive_time else None,
        }