# Generated by Django 4.1.7 on 2023-06-09 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0018_purchasedproduct'),
        ('Cart', '0009_alter_purchasehistory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refund', to='Product.purchasedproduct'),
        ),
    ]
