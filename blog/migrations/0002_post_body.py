# Generated by Django 3.2.6 on 2021-08-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
