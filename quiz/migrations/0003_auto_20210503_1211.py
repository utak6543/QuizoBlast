# Generated by Django 3.1.7 on 2021-05-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210503_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default='general', max_length=100),
        ),
    ]
