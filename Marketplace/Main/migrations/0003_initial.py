# Generated by Django 4.1.7 on 2023-06-03 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0002_delete_anonuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('ID', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('balance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]