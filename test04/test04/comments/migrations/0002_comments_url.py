# Generated by Django 2.2.3 on 2019-12-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
