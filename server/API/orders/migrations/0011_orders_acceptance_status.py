# Generated by Django 3.0.6 on 2020-09-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200824_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Acceptance_Status',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default='', null=True),
        ),
    ]
