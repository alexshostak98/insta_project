# Generated by Django 4.0.3 on 2022-03-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_app', '0001_initial'),
        ('hashtag_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='comment',
            field=models.ManyToManyField(related_name='hashtag', to='comment_app.comment'),
        ),
    ]