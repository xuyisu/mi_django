from django import forms

from apps.user_address import models


# 用户地址表单验证
class UserAddressForm(forms.ModelForm):
    # 收货人
    receiveName = forms.CharField(
        max_length=60,
        error_messages={
            'required': '收货人不能为空',
            'max_length': '收货人不能为空不得超过60个字符',
        }
    )
    # 联系号码
    receivePhone = forms.CharField(
        max_length=20,
        error_messages={
            'required': '联系号码不能为空',
            'max_length': '联系号码长度不得超过20个字符',
        }
    )
    # 省份
    province = forms.CharField(
        max_length=20,
        error_messages={
            'required': '省份能为空',
            'max_length': '省份编码不得超过20个字符',
        }
    )
    # 省份编码
    provinceCode = forms.CharField(
        max_length=10,
        error_messages={
            'required': '省份编码不能为空',
            'max_length': '省份编码不得超过10个字符',
        }
    )
    # 城市
    city = forms.CharField(
        max_length=20,
        error_messages={
            'required': '城市不能为空',
            'max_length': '城市长度不得超过20个字符',
        }
    )
    # 城市编码
    cityCode = forms.CharField(
        max_length=10,
        error_messages={
            'required': '城市编码不能为空',
            'max_length': '城市编码长度不得超过10个字符',
        }
    )
    # 区
    area = forms.CharField(
        max_length=20,
        error_messages={
            'required': '区不能为空',
            'max_length': '区长度不得超过20个字符',
        }
    )
    # 区编码
    areaCode = forms.CharField(
        max_length=10,
        error_messages={
            'required': '区编码不能为空',
            'max_length': '区编码不得超过10个字符',
        }
    )
    # 详细地址
    street = forms.CharField(
        max_length=100,
        error_messages={
            'required': '详细地址不能为空',
            'max_length': '详细地址不得超过100个字符',
        }
    )

    # 默认标志
    defaultFlag = forms.IntegerField(
        max_value=1,
        min_value=0,
        error_messages={
            'required': '默认标志不能为空',
            'min_value': '默认标志不得小于0',
            'max_value': '默认标志不得大于1',
        }
    )

    # 邮编
    postalCode = forms.CharField(
        max_length=10,
        error_messages={
            'required': '邮编不能为空',
            'max_length': '邮编不得超过10个字符',
        }
    )

    # 地址标签
    addressLabel = forms.IntegerField(
        max_value=127,
        min_value=0,
        error_messages={
            'required': '地址标签不能为空',
            'min_value': '地址标签不得小于0',
            'max_value': '地址标签不得大于127',
        }
    )

    class Meta:
        # 绑定模型
        model = models.UserAddress
        # 指定部分字段验证
        fields = ['receiveName', 'receivePhone', 'provinceCode', 'city', 'cityCode', 'area', 'areaCode', 'street']

# # 用户状态设置
# class UserStatusForm(forms.ModelForm):
#     # 用户ID
#     id = forms.IntegerField(
#         min_value=1,
#         error_messages={
#             'required': '用户ID不能为空',
#             'min_value': '用户ID不得小于1',
#         }
#     )
#     # 用户状态：1-正常 2-禁用
#     status = forms.IntegerField(
#         min_value=1,
#         max_value=2,
#         error_messages={
#             'required': '用户状态不能为空',
#             'min_value': '用户状态值在1~2之间',
#             'max_value': '用户状态值在1~2之间',
#         }
#     )
#
#     class Meta:
#         # 绑定模型
#         model = models.User
#         # 指定部分字段验证
#         fields = ["id", "status"]
