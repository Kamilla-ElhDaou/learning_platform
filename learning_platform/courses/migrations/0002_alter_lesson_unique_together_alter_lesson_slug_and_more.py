# Generated by Django 4.2.19 on 2025-03-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='URL'),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('course', 'slug')},
        ),
    ]
