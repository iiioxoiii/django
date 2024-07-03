# Generated by Django 4.2 on 2024-07-01 18:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasaga', '0009_oferta_estudi_estudis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modul',
            name='codi',
        ),
        migrations.AddField(
            model_name='modul',
            name='estudi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ultrasaga.estudi'),
            preserve_default=False,
        ),
    ]