# Generated by Django 4.1.7 on 2023-06-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0014_alter_comment_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='instockproduct',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='instockproduct',
            name='purchased_price',
            field=models.IntegerField(default=0),
        ),
    ]