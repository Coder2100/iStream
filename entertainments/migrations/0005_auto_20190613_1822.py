# Generated by Django 2.2 on 2019-06-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0004_remove_comedy_commic_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='position',
        ),
        migrations.AlterField(
            model_name='comedy',
            name='upload_comedy',
            field=models.FileField(upload_to='audios/'),
        ),
    ]
