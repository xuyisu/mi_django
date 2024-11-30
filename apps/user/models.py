from django.db import models

from apps.base_model import BaseModel


# 用户模型
class User(BaseModel):
    # 启用标志
    status = models.BooleanField(default=True, verbose_name='启用标志')  # 同样转换为布尔值
    # 用户名
    user_name = models.CharField(max_length=50, default='', verbose_name='用户名')
    # 邮箱
    email = models.EmailField(max_length=50, default='', verbose_name='邮箱')  # 使用EmailField验证邮箱格式
    # 手机号
    phone = models.CharField(max_length=20, unique=True, verbose_name='手机号')  # 唯一约束直接在字段上设置
    # 密码
    password = models.CharField(max_length=100, default='', verbose_name='密码')

    class Meta:
            # 数据表名
            db_table = "user"
            verbose_name = "用户表"
            verbose_name_plural = verbose_name

    def __str__(self):
        return "用户{}".format(self.id)