# Generated by Django 3.2.5 on 2021-07-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_alter_invoice_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
