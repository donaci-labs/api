# Generated by Django 2.1.3 on 2018-11-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
