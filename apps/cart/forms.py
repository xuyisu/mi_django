from django import forms

from apps.cart import models


# 添加购物车请求
class CartAddForm(forms.ModelForm):
    # 商品id
    productId = forms.CharField(
        error_messages={
            'required': '商品id不能为空',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Cart
        # 指定部分字段验证
        fields = ['productId']


# 修改购物车请求
class CartUpdateForm(forms.ModelForm):
    # 数量
    quantity = forms.CharField(
        error_messages={
            'required': '数量不能为空',
        }
    )
    # 是否选中
    selected = forms.IntegerField(
        error_messages={
            'required': '是否选中不能为空',
        }
    )
    # 类型
    type = forms.IntegerField(
        error_messages={
            'required': '类型不能为空',
        }
    )

    class Meta:
        # 绑定模型
        model = models.Cart
        # 指定部分字段验证
        fields = ['type']
