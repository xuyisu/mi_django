# Generated by Django 5.1.1 on 2024-09-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('delete_flag', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('default_flag', models.SmallIntegerField(default=0, null=True, verbose_name='默认标志')),
                ('receive_name', models.CharField(default='', max_length=60, verbose_name='收货人')),
                ('receive_phone', models.CharField(default='', max_length=20, verbose_name='联系号码')),
                ('province', models.CharField(default='', max_length=20, verbose_name='省份')),
                ('province_code', models.CharField(default='', max_length=10, verbose_name='省份编码')),
                ('city', models.CharField(default='', max_length=20, verbose_name='城市')),
                ('city_code', models.CharField(default='', max_length=10, verbose_name='城市编码')),
                ('area', models.CharField(default='', max_length=20, verbose_name='区')),
                ('area_code', models.CharField(default='', max_length=10, verbose_name='区编码')),
                ('street', models.CharField(default='', max_length=100, null=True, verbose_name='详细地址')),
                ('postal_code', models.CharField(default='', max_length=10, null=True, verbose_name='邮编')),
                ('address_label', models.SmallIntegerField(default=0, null=True, verbose_name='地址标签')),
            ],
            options={
                'verbose_name': '用户地址',
                'verbose_name_plural': '用户地址',
                'db_table': 'user_address',
            },
        ),
    ]
