# Generated by Django 4.2.2 on 2023-08-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_productdetails_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchesdetails',
            name='confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='purchesdetails',
            name='product_code',
            field=models.CharField(editable=False, max_length=15, unique=True),
        ),
    ]
