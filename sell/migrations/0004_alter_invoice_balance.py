# Generated by Django 3.2.5 on 2021-07-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_invoice_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='balance',
            field=models.TextField(max_length=100, null=True),
        ),
    ]