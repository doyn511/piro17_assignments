# Generated by Django 4.0.6 on 2022-07-20 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='interset',
            new_name='interest',
        ),
    ]
