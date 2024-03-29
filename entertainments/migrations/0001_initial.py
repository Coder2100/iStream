# Generated by Django 2.2 on 2019-06-15 22:00

from django.db import migrations, models
import entertainments.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('comedian', models.CharField(max_length=250)),
                ('released_date', models.DateField()),
                ('distribution_rights', models.TextField()),
                ('about_jokes', models.TextField()),
                ('cover_image', models.ImageField(upload_to='images/', validators=[entertainments.validators.image_validation_extension])),
                ('upload_comedy', models.FileField(upload_to='audios/', validators=[entertainments.validators.video_validation_extention])),
            ],
        ),
        migrations.CreateModel(
            name='CommunityContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('thumbnail', models.ImageField(upload_to='images/community', validators=[entertainments.validators.image_validation_extension])),
                ('video', models.FileField(upload_to='audios/community', validators=[entertainments.validators.video_validation_extention])),
                ('posted_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('film_type', models.CharField(choices=[('D', 'Drama'), ('S', 'Sitcom'), ('PD', 'Podcast Video'), ('SR', 'Series'), ('RS', 'Reality TV Show'), ('H', 'Home Entertainment')], default='Home Entertainment', max_length=60)),
                ('details', models.TextField()),
                ('movie', models.FileField(upload_to='videos/', validators=[entertainments.validators.video_validation_extention])),
                ('cover_image', models.ImageField(upload_to='images/', validators=[entertainments.validators.image_validation_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('released_date', models.DateField()),
                ('distribution_rights', models.TextField()),
                ('music_genre', models.CharField(choices=[('P', 'POP'), ('G', 'GOSPEL'), ('R', 'ROCK'), ('AP', 'AFRO POP'), ('RG', 'REGGAE'), ('H', 'HOUSE'), ('GN', 'GENERIC')], default='GENERIC', max_length=60)),
                ('cover_image', models.ImageField(upload_to='images/', validators=[entertainments.validators.image_validation_extension])),
                ('song', models.FileField(upload_to='audios/', validators=[entertainments.validators.video_validation_extention])),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcast_name', models.CharField(max_length=250)),
                ('broadcaster', models.CharField(max_length=250)),
                ('released_date', models.DateField()),
                ('distribution_rights', models.TextField()),
                ('podcast_genre', models.CharField(choices=[('L', 'Life Advice'), ('F', 'Personal Finance'), ('A', 'Academic Performance'), ('O', 'Other')], default='Other', max_length=60)),
                ('cover_image', models.ImageField(upload_to='images/', validators=[entertainments.validators.image_validation_extension])),
                ('upload_podcast', models.FileField(upload_to='audios/', validators=[entertainments.validators.video_validation_extention])),
            ],
        ),
    ]
