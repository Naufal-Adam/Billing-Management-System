# Generated by Django 4.2.3 on 2023-08-16 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_rename_klient_produk_client'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_notif', models.DateField(null=True)),
                ('time_notif', models.TimeField(null=True)),
                ('text_notif', models.TextField(null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('produk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.produk')),
            ],
        ),
    ]
