# Generated by Django 4.2.3 on 2023-08-09 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0002_rename_klient_produk_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_invoice', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('produk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.produk')),
            ],
        ),
    ]