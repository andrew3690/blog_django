# Generated by Django 3.0.5 on 2020-04-25 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('country_code', models.CharField(max_length=2, verbose_name='country code')),
                ('created', models.DateField(verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('color', models.CharField(max_length=30, verbose_name='color')),
                ('description', models.TextField(verbose_name='description')),
                ('type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Truck'), (3, 'SUV')], verbose_name='type')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Manufacturer', verbose_name='manufacturer')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
