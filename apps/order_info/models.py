from django.db import models

from apps.base_model import BaseModel


# 订单模型
class OrderInfo(BaseModel):
    # 订单编号
    order_no = models.CharField(max_length=60, default='', verbose_name='订单编号')
    # 支付金额
    payment = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, null=True, verbose_name='支付金额')
    # 支付类型
    payment_type = models.SmallIntegerField(default=0, null=True, verbose_name='支付类型')
    # 支付类型描述
    payment_type_desc = models.CharField(max_length=20, default='', null=True, verbose_name='支付类型描述')
    # 邮费
    postage = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, null=True, verbose_name='邮费')
    # 订单状态
    status = models.SmallIntegerField(default=0, verbose_name='订单状态')
    # 状态描述
    status_desc = models.CharField(max_length=20, default='', verbose_name='状态描述')
    # 支付时间
    payment_time = models.DateTimeField(null=True, verbose_name='支付时间')
    # 地址id
    address_id = models.BigIntegerField(default=0, null=True, verbose_name='地址id')
    # 收货人
    receive_name = models.CharField(max_length=50, default='', null=True, verbose_name='收货人')
    # 联系号码
    receive_phone = models.CharField(max_length=20, default='', null=True, verbose_name='联系号码')
    # 省份
    province = models.CharField(max_length=20, default='', null=True, verbose_name='省份')
    # 城市
    city = models.CharField(max_length=20, default='', null=True, verbose_name='城市')
    # 区
    area = models.CharField(max_length=20, default='', null=True, verbose_name='区')
    # 详细地址
    street = models.CharField(max_length=50, default='', null=True, verbose_name='详细地址')
    # 邮编
    postal_code = models.CharField(max_length=255, default='', null=True, verbose_name='邮编')
    # 用户ig
    user_id = models.BigIntegerField(default=0, null=True, verbose_name='用户id')

    class Meta:
        db_table = 'order_info'  # 指定数据库中的表名
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_no

    def to_dict(self):
        return {
            'id': self.id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            'createUser': self.create_user,
            'updateUser': self.update_user,
            'orderNo': self.order_no,
            'payment': self.payment,
            'paymentYype': self.payment_type,
            'paymentTypeDesc': self.payment_type_desc,
            'postage': self.postage,
            'status': self.status,
            'statusDesc': self.status_desc,
            'paymentTime': self.payment_time.isoformat() if self.payment_time else None,
            'addressId': self.address_id,
            'receiveName': self.receive_name,
            'receivePhone': self.receive_phone,
            'province': self.province,
            'city': self.city,
            'area': self.area,
            'street': self.street,
            'postalCode': self.postal_code,
            'user_id': self.user_id,
            'details': []
        }
