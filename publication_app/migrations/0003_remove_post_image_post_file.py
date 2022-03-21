# Generated by Django 4.0.3 on 2022-03-21 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
        ('publication_app', '0002_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='media_app.media'),
            preserve_default=False,
        ),
    ]