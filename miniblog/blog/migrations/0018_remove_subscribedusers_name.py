# Generated by Django 4.1.2 on 2023-02-17 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_delete_idcreator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribedusers',
            name='name',
        ),
    ]
