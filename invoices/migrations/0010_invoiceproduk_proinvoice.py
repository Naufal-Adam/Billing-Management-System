# Generated by Django 4.2.3 on 2023-08-11 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_alter_invoice_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceproduk',
            name='proinvoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice'),
        ),
    ]
