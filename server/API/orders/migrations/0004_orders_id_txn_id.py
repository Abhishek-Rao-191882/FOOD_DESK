# Generated by Django 3.0.6 on 2020-08-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200821_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_id',
            name='TXN_ID',
            field=models.BigIntegerField(default=-2),
            preserve_default=False,
        ),
    ]