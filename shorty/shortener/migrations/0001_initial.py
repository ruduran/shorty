# Generated by Django 2.0.7 on 2018-07-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('code', models.CharField(db_index=True, max_length=32, unique=True)),
            ],
        ),
    ]
