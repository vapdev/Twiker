# Generated by Django 4.1.3 on 2023-02-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twikkerprofile', '0006_alter_twikkerprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='twikkerprofile',
            name='biography',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Biografia do usuário'),
        ),
    ]