# Generated by Django 4.1.2 on 2022-11-06 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_alter_tweek_retweek'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tweek',
            unique_together={('id', 'retweek')},
        ),
    ]