from django.db import models

from apps.base_model import BaseModel


# 用户模型
class Category(BaseModel):
    # 父id
    parent_id = models.BigIntegerField(default=0, null=True, blank=True, verbose_name='父id')
    # 名称
    name = models.CharField(max_length=100, default='', blank=True, verbose_name='名称')
    # 启用禁用状态 1启用 0禁用
    status = models.SmallIntegerField(default=0, null=True, blank=True, verbose_name='启用禁用状态 1启用 0禁用')
    # 排序
    sort_order = models.IntegerField(default=0, null=True, blank=True, verbose_name='排序')

    class Meta:
        db_table = 'category'
        verbose_name = '类目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def to_dict(self):
        # 使用字典推导式来生成字典
        return {
            'id': self.id,
            'createTime': str(self.create_time.strftime('%Y-%m-%d %H:%M:%S')) if self.create_time else None,
            'updateTime': str(self.update_time.strftime('%Y-%m-%d %H:%M:%S')) if self.update_time else None,
            'createUser': self.create_user,
            'updateUser': self.update_user,
            'parentId': self.parent_id,
            'name': self.name,
            'status': self.status,
            'sortOrder': self.sort_order,
        }