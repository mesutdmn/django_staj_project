# Generated by Django 4.0.3 on 2022-05-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_article_etkinlik_tarihi'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeritabaniSertifikalar',
            fields=[
                ('sertifika_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Sertifika ID')),
            ],
        ),
    ]