# Generated by Django 3.0.5 on 2020-04-30 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200429_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={},
        ),
        migrations.RemoveField(
            model_name='blog_post',
            name='title',
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='text',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='subject',
            name='tag',
            field=models.CharField(max_length=125),
        ),
    ]
