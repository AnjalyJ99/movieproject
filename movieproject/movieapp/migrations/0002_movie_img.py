# Generated by Django 4.1 on 2022-10-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ftfjh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
