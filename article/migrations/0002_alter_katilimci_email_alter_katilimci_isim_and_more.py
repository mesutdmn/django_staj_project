# Generated by Django 4.0.3 on 2022-04-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='katilimci',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='katilimci',
            name='isim',
            field=models.CharField(max_length=50, verbose_name='isim'),
        ),
        migrations.AlterField(
            model_name='katilimci',
            name='soy_isim',
            field=models.CharField(max_length=50, verbose_name='soy_isim '),
        ),
        migrations.AlterField(
            model_name='katilimci',
            name='tc_no',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='tc_no'),
        ),
    ]