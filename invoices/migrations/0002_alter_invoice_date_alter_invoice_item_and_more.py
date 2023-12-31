# Generated by Django 4.2.3 on 2023-08-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='item',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='no_invoice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='subtotal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
