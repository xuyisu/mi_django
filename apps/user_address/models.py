from django.db import models

from apps.base_model import BaseModel


# 用户地址
class UserAddress(BaseModel):
    # 地址id
    address_id = models.BigIntegerField(default=0, verbose_name='地址id')
    # 默认标志
    default_flag = models.SmallIntegerField(default=0, null=True, verbose_name='默认标志')
    # 收货人
    receive_name = models.CharField(max_length=60, default='', verbose_name='收货人')
    # 联系号码
    receive_phone = models.CharField(max_length=20, default='', verbose_name='联系号码')
    # 省份
    province = models.CharField(max_length=20, default='', verbose_name='省份')
    # 省份编码
    province_code = models.CharField(max_length=10, default='', verbose_name='省份编码')
    # 城市
    city = models.CharField(max_length=20, default='', verbose_name='城市')
    # 城市编码
    city_code = models.CharField(max_length=10, default='', verbose_name='城市编码')
    # 区
    area = models.CharField(max_length=20, default='', verbose_name='区')
    # 区编码
    area_code = models.CharField(max_length=10, default='', verbose_name='区编码')
    # 详细地址
    street = models.CharField(max_length=100, default='', null=True, verbose_name='详细地址')
    # 邮编
    postal_code = models.CharField(max_length=10, default='', null=True, verbose_name='邮编')
    # 地址标签
    address_label = models.SmallIntegerField(default=0, null=True, verbose_name='地址标签')

    class Meta:
        db_table = 'user_address'
        verbose_name = '用户地址'
        verbose_name_plural = '用户地址'

    def __str__(self):
        return f"{self.receive_name} - {self.province} {self.city} {self.area}"

    def to_dict(self):
        # 使用字典推导式来生成字典
        return {
            'id': self.id,
            'addressId': self.address_id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            'createUser': self.create_user,
            'updateUser': self.update_user,
            'deleteFlag': self.delete_flag,
            'defaultFlag': self.default_flag,
            'receiveName': self.receive_name,
            'receivePhone': self.receive_phone,
            'province': self.province,
            'provinceCode': self.province_code,
            'city': self.city,
            'cityCode': self.city_code,
            'area': self.area,
            'areaCode': self.area_code,
            'street': self.street,
            'postalCode': self.postal_code,
            'addressLabel': self.address_label,
        }
