# Generated by Django 4.0.3 on 2022-04-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0012_rename_chapter_manga_chapters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='chapters',
            field=models.ManyToManyField(blank=True, related_name='manychapter', to='mangas.chapter'),
        ),
    ]
