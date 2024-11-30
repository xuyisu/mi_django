# Generated by Django 5.1.1 on 2024-09-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('create_user', models.IntegerField(default=0, verbose_name='创建人')),
                ('create_time', models.DateTimeField(auto_now_add=True, max_length=11, null=True, verbose_name='创建时间')),
                ('update_user', models.IntegerField(default=0, verbose_name='更新人')),
                ('update_time', models.DateTimeField(auto_now=True, max_length=11, null=True, verbose_name='更新时间')),
                ('delete_flag', models.BooleanField(default=0, verbose_name='逻辑删除')),
                ('status', models.BooleanField(default=True, verbose_name='启用标志')),
                ('user_name', models.CharField(default='', max_length=50, verbose_name='用户名')),
                ('email', models.EmailField(default='', max_length=50, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='手机号')),
                ('password', models.CharField(default='', max_length=100, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'user',
            },
        ),
    ]