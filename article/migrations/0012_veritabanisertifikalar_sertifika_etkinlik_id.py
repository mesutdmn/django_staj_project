# Generated by Django 4.0.3 on 2022-05-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_veritabanisertifikalar'),
    ]

    operations = [
        migrations.AddField(
            model_name='veritabanisertifikalar',
            name='sertifika_etkinlik_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Etkinlik ID'),
        ),
    ]
