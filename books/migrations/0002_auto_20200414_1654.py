# Generated by Django 3.0.5 on 2020-04-14 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-c_time'], 'verbose_name': '书', 'verbose_name_plural': '书'},
        ),
    ]
