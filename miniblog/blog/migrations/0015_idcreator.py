# Generated by Django 4.1.2 on 2022-11-16 11:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_contactus_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idcreator',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Idcreator',
                'verbose_name_plural': 'Idcreator',
            },
        ),
    ]
