from django.db import models

from apps.base_model import BaseModel


# 活动模型
class Activity(BaseModel):
    # 活动id
    activity_id = models.BigIntegerField(default=0, verbose_name='活动id', unique=True)
    # 活动名称
    name = models.CharField(max_length=60, null=True, blank=True, verbose_name='活动名称')
    # 活动状态
    status = models.IntegerField(default=0, verbose_name='活动状态')
    # 活动图片地址
    main_image = models.CharField(max_length=100, null=True, blank=True, verbose_name='活动图片地址')
    # 开始时间
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='开始时间')
    # 结束时间
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='结束时间')

    class Meta:
            # 数据表名
            db_table = "activity"
            verbose_name = "活动表"
            verbose_name_plural = verbose_name

    def __str__(self):
        return "活动{}".format(self.id)