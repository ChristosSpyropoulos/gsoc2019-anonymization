# Generated by Django 2.0.7 on 2019-07-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_file', '0011_auto_20190717_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
