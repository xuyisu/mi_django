# Generated by Django 5.1.1 on 2024-09-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('delete_flag', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('order_no', models.CharField(default='', max_length=60, verbose_name='订单编号')),
                ('payment', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True, verbose_name='支付金额')),
                ('payment_type', models.SmallIntegerField(default=0, null=True, verbose_name='支付类型')),
                ('payment_type_desc', models.CharField(default='', max_length=20, null=True, verbose_name='支付类型描述')),
                ('postage', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, null=True, verbose_name='邮费')),
                ('status', models.SmallIntegerField(default=0, verbose_name='订单状态')),
                ('status_desc', models.CharField(default='', max_length=20, verbose_name='状态描述')),
                ('payment_time', models.DateTimeField(null=True, verbose_name='支付时间')),
                ('address_id', models.BigIntegerField(default=0, null=True, verbose_name='地址id')),
                ('receive_name', models.CharField(default='', max_length=50, null=True, verbose_name='收货人')),
                ('receive_phone', models.CharField(default='', max_length=20, null=True, verbose_name='联系号码')),
                ('province', models.CharField(default='', max_length=20, null=True, verbose_name='省份')),
                ('city', models.CharField(default='', max_length=20, null=True, verbose_name='城市')),
                ('area', models.CharField(default='', max_length=20, null=True, verbose_name='区')),
                ('street', models.CharField(default='', max_length=50, null=True, verbose_name='详细地址')),
                ('postal_code', models.CharField(default='', max_length=255, null=True, verbose_name='邮编')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'order_info',
            },
        ),
    ]
