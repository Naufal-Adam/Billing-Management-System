# Generated by Django 4.2.3 on 2023-08-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_alter_invoice_date_alter_invoice_item_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='date',
            new_name='invoice_date',
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_due_date',
            field=models.DateField(null=True),
        ),
    ]
