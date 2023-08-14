# Generated by Django 4.2.3 on 2023-08-10 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_klient_produk_client'),
        ('invoices', '0007_invoiceproduk_remove_invoice_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='produk',
        ),
        migrations.AddField(
            model_name='invoiceproduk',
            name='produk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.produk'),
        ),
    ]
