# Generated by Django 4.2.1 on 2023-11-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
