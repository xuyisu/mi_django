# Generated by Django 5.1.1 on 2024-09-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('delete_flag', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('user_id', models.BigIntegerField(blank=True, null=True, verbose_name='用户id')),
                ('activity_id', models.BigIntegerField(blank=True, null=True, verbose_name='活动id')),
                ('activity_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='活动名称')),
                ('product_id', models.BigIntegerField(verbose_name='商品id')),
                ('product_name', models.CharField(max_length=255, verbose_name='商品名称')),
                ('product_subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品简要描述')),
                ('product_main_image', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品图片地址')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='数量')),
                ('product_unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='单价')),
                ('selected', models.BooleanField(default=True, verbose_name='是否已选择')),
                ('product_total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='总价格')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'cart',
            },
        ),
    ]
