# Generated by Django 3.0.6 on 2020-08-02 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Seller_Id',
            new_name='Client_Id',
        ),
    ]
