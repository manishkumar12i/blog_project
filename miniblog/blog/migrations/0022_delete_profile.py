# Generated by Django 4.1.7 on 2023-03-25 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_profile_delete_set_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
