from django import forms

from apps.order_info import models


# 订单创建验证
class OrderCreateForm(forms.ModelForm):
    # 地址id
    addressId = forms.CharField(
        error_messages={
            'required': '地址id不能为空',
        }
    )

    class Meta:
        # 绑定模型
        model = models.OrderInfo
        # 指定部分字段验证
        fields = ['addressId']

# 订单付款验证
class OrderPayForm(forms.ModelForm):
    # 地址id
    orderNo = forms.CharField(
        error_messages={
            'required': '订单编号不能为空',
        }
    )

    class Meta:
        # 绑定模型
        model = models.OrderInfo
        # 指定部分字段验证
        fields = ['orderNo']
