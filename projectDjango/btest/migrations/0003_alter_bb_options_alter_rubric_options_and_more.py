# Generated by Django 4.1.2 on 2022-11-06 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Выставочные залы', 'verbose_name_plural': 'Выставочные залы'},
        ),
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ['name'], 'verbose_name': 'Коллекции', 'verbose_name_plural': 'Коллекции'},
        ),
        migrations.RemoveField(
            model_name='bb',
            name='rubric',
        ),
    ]
