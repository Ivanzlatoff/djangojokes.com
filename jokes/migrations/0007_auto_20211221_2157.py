# Generated by Django 3.2.9 on 2021-12-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0006_auto_20211221_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag']},
        ),
        migrations.AlterField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(blank=True, to='jokes.Tag'),
        ),
    ]
