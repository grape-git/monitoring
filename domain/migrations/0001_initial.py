# Generated by Django 3.2.4 on 2021-06-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=150, verbose_name='URL 이름')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Url',
                'db_table': 'url_model',
            },
        ),
    ]
