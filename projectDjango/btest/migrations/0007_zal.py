# Generated by Django 4.1.2 on 2022-11-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0006_collection_content_collection_fin_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Выставочный зал',
                'verbose_name_plural': 'Выставочные залы',
                'ordering': ['name'],
            },
        ),
    ]
