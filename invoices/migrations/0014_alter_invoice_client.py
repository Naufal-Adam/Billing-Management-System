# Generated by Django 4.2.3 on 2023-08-11 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('invoices', '0013_remove_invoiceproduk_proinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]
