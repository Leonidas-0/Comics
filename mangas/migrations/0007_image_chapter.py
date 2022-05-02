# Generated by Django 4.0.3 on 2022-04-04 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0006_remove_manga_rating_manga_rating_alter_rating_manga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ManyToManyField(null=True, to='mangas.image')),
                ('manga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mangachapters', to='mangas.manga')),
            ],
        ),
    ]