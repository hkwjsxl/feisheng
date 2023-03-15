# Generated by Django 3.2.18 on 2023-03-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='姓名/名称/标题')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('orders', models.SmallIntegerField(default=0, verbose_name='序号')),
                ('image', models.ImageField(upload_to='banner/%Y/', verbose_name='图片地址')),
                ('link', models.CharField(max_length=500, verbose_name='链接地址')),
                ('note', models.CharField(max_length=150, verbose_name='备注信息')),
                ('is_http', models.BooleanField(default=False, verbose_name='是否外链地址')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'fs_banner',
            },
        ),
    ]
