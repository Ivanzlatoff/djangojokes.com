# Generated by Django 3.2.9 on 2021-12-27 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jokes', '0007_auto_20211221_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='users.customuser'),
            preserve_default=False,
        ),
    ]
