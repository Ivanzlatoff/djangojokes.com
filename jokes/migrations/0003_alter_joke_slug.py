# Generated by Django 3.2.9 on 2021-12-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0002_joke_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='slug',
            field=models.SlugField(default='foo', editable=False, unique=True),
            preserve_default=False,
        ),
    ]