# Generated by Django 4.1.7 on 2023-03-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instockproduct",
            name="image",
            field=models.ImageField(upload_to="Main/static/img/"),
        ),
    ]
