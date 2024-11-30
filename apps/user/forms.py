from django import forms

from apps.user import models


# 用户表单验证
class UserRegisterForm(forms.ModelForm):
    # 手机号
    phone = forms.CharField(
        max_length=11,
        error_messages={
            'required': '手机号不能为空',
            'max_length': '手机号长度不得超过11个字符',
        }
    )
    # 邮箱
    email = forms.CharField(
        max_length=30,
        error_messages={
            'required': '邮箱不能为空',
            'max_length': '邮箱长度不得超过30个字符',
        }
    )
    # 用户名
    userName = forms.CharField(
        max_length=30,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '用户名长度不得超过30个字符',
        }
    )
    # 密码
    password = forms.CharField(
        required=False,
        max_length=30,
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码长度不得超过30个字符',
        }
    )



    class Meta:
        # 绑定模型
        model = models.User
        # 指定部分字段验证
        fields = ['phone', 'email', 'userName', 'password']


# 用户状态设置
class UserLoginForm(forms.ModelForm):
    # 用户ID
    userName = forms.CharField(
        max_length=30,
        error_messages={
            'required': '用户名不能为空',
            'max_length': '用户名长度不得超过30个字符',
        }
    )
    # 用户状态：1-正常 2-禁用
    password = forms.CharField(
        max_length=255,
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码长度不得超过255个字符',
        }
    )

    class Meta:
        # 绑定模型
        model = models.User
        # 指定部分字段验证
        fields = ["userName", "password"]
