# Generated by Django 4.1.7 on 2023-04-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="home_address",
            field=models.TextField(blank=True, null=True),
        ),
    ]
