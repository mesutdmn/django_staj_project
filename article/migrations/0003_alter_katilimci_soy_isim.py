# Generated by Django 4.0.3 on 2022-04-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_katilimci_email_alter_katilimci_isim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katilimci',
            name='soy_isim',
            field=models.CharField(max_length=50, verbose_name='soy_isim'),
        ),
    ]
