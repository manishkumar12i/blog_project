# Generated by Django 4.1.2 on 2022-10-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
