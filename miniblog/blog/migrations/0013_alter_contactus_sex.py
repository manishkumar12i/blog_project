# Generated by Django 4.1.2 on 2022-10-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20, null=True),
        ),
    ]
