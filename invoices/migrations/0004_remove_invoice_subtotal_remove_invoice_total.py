# Generated by Django 4.2.3 on 2023-08-10 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_rename_date_invoice_invoice_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='total',
        ),
    ]
