# Generated by Django 5.1.1 on 2024-09-18 03:36

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('delete_flag', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('order_no', models.CharField(default='', max_length=60, verbose_name='订单编号')),
                ('order_detail_no', models.CharField(default='', max_length=60, verbose_name='订单明细编号')),
                ('activity_id', models.BigIntegerField(blank=True, default=0, null=True, verbose_name='活动id')),
                ('activity_name', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='活动名称')),
                ('activity_main_image', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='活动图片地址')),
                ('product_id', models.BigIntegerField(default=0, verbose_name='商品id')),
                ('product_name', models.CharField(default='', max_length=50, verbose_name='商品名称')),
                ('product_main_image', models.CharField(default='', max_length=100, verbose_name='商品图片地址')),
                ('current_unit_price', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=20, null=True, verbose_name='单价')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='数量')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=20, null=True, verbose_name='总价')),
                ('user_id', models.BigIntegerField(default=0, verbose_name='购买人id')),
                ('status', models.SmallIntegerField(default=0, verbose_name='订单状态')),
                ('status_desc', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='状态描述')),
                ('cancel_time', models.DateTimeField(blank=True, null=True, verbose_name='取消时间')),
                ('cancel_reason', models.IntegerField(blank=True, default=0, null=True, verbose_name='取消原因')),
                ('send_time', models.DateTimeField(blank=True, null=True, verbose_name='发货时间')),
                ('receive_time', models.DateTimeField(blank=True, null=True, verbose_name='签收时间')),
            ],
            options={
                'verbose_name': '订单明细',
                'verbose_name_plural': '订单明细',
                'db_table': 'order_detail',
            },
        ),
    ]