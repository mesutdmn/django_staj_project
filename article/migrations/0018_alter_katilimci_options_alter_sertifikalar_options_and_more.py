# Generated by Django 4.0.3 on 2022-05-05 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='katilimci',
            options={'ordering': ['-tc_no']},
        ),
        migrations.AlterModelOptions(
            name='sertifikalar',
            options={'ordering': ['-etkinlik_id']},
        ),
        migrations.AlterModelOptions(
            name='veritabanisertifikalar',
            options={'ordering': ['-sertifika_id']},
        ),
    ]