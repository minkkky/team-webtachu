# Generated by Django 4.0.5 on 2022-06-07 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=20)),
                ('story', models.TextField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
