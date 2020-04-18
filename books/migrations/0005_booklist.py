# Generated by Django 3.0.5 on 2020-04-15 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200414_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('listid', models.AutoField(primary_key=True, serialize=False)),
                ('listtitle', models.CharField(max_length=100)),
                ('listcontents', models.TextField()),
                ('c_time', models.DateTimeField()),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books')),
            ],
            options={
                'verbose_name': '目录',
                'verbose_name_plural': '目录',
                'ordering': ['-c_time'],
            },
        ),
    ]
