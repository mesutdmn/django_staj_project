# Generated by Django 4.0.3 on 2022-05-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_alter_katilimci_options_alter_sertifikalar_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='goster',
            field=models.BooleanField(default=True, verbose_name='Ana Sayfada Göster'),
        ),
    ]
