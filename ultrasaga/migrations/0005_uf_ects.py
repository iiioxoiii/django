# Generated by Django 4.2 on 2024-07-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasaga', '0004_remove_uf_ects'),
    ]

    operations = [
        migrations.AddField(
            model_name='uf',
            name='ects',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
    ]