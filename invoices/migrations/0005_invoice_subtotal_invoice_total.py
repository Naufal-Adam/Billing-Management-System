# Generated by Django 4.2.3 on 2023-08-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_remove_invoice_subtotal_remove_invoice_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='subtotal',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
