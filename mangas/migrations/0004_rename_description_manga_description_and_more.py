# Generated by Django 4.0.3 on 2022-04-04 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0003_category_manga_rating_manga_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='category',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='Title',
            new_name='title',
        ),
    ]