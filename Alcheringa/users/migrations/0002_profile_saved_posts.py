# Generated by Django 3.2.9 on 2022-08-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlcherWeb', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='saved_posts',
            field=models.ManyToManyField(related_name='sp', to='AlcherWeb.Post'),
        ),
    ]