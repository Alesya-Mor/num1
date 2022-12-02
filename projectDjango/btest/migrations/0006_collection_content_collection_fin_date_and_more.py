# Generated by Django 4.1.2 on 2022-11-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0005_collection_alter_bb_options_alter_exponat_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='collection',
            name='fin_date',
            field=models.DateTimeField(null=True, verbose_name='Период показа'),
        ),
        migrations.AddField(
            model_name='collection',
            name='start_date',
            field=models.DateTimeField(null=True, verbose_name='Период показа'),
        ),
        migrations.AddField(
            model_name='exponat',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='exponat',
            name='dlina',
            field=models.FloatField(blank=True, null=True, verbose_name='Длина'),
        ),
        migrations.AddField(
            model_name='exponat',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='exponat',
            name='shirina',
            field=models.FloatField(blank=True, null=True, verbose_name='Ширина'),
        ),
        migrations.AddField(
            model_name='exponat',
            name='stoimost',
            field=models.FloatField(blank=True, null=True, verbose_name='Страховая стоимость'),
        ),
        migrations.AddField(
            model_name='exponat',
            name='vek_sozdania',
            field=models.FloatField(blank=True, null=True, verbose_name='Век создания'),
        ),
        migrations.AddField(
            model_name='exponat',
            name='visota',
            field=models.FloatField(blank=True, null=True, verbose_name='Высота'),
        ),
    ]