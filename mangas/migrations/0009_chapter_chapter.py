# Generated by Django 4.0.3 on 2022-04-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0008_manga_chapter_alter_chapter_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter',
            field=models.IntegerField(null=True),
        ),
    ]
