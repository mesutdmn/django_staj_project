# Generated by Django 4.0.3 on 2022-05-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_sertifikalar'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='etkinlik_tarihi',
            field=models.DateField(blank=True, null=True, verbose_name='Etkinlik Tarihi'),
        ),
    ]