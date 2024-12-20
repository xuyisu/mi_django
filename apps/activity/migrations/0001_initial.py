# Generated by Django 5.1.1 on 2024-09-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('delete_flag', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('activity_id', models.BigIntegerField(default=0, unique=True, verbose_name='活动id')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='活动名称')),
                ('status', models.IntegerField(default=0, verbose_name='活动状态')),
                ('main_image', models.CharField(blank=True, max_length=100, null=True, verbose_name='活动图片地址')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '活动表',
                'verbose_name_plural': '活动表',
                'db_table': 'activity',
            },
        ),
    ]
