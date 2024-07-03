# Generated by Django 4.2 on 2024-07-01 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ultrasaga', '0008_estudi_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('any_oferta', models.IntegerField()),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultrasaga.escola')),
                ('estudi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultrasaga.estudi')),
            ],
        ),
        migrations.AddField(
            model_name='estudi',
            name='estudis',
            field=models.ManyToManyField(through='ultrasaga.Oferta', to='ultrasaga.estudi'),
        ),
    ]