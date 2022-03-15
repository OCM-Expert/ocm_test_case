# Generated by Django 3.2.12 on 2022-03-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_useremails_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremails',
            name='mes_text',
            field=models.TextField(blank=True, verbose_name='Message text'),
        ),
        migrations.AlterField(
            model_name='useremails',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Delivered status'),
        ),
    ]
