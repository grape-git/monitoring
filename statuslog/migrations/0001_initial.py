# Generated by Django 3.2.4 on 2021-06-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('domain', '0002_auto_20210611_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=10, verbose_name='상태코드')),
                ('process', models.CharField(max_length=100, verbose_name='처리시간')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.urlmodel', verbose_name='Url')),
            ],
            options={
                'verbose_name': '상태로그',
                'verbose_name_plural': '상태로그',
                'db_table': 'url_status',
            },
        ),
    ]
