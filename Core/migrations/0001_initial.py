# Generated by Django 3.2.2 on 2021-05-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Sender Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Sender Email')),
                ('message', models.TextField(verbose_name='Message')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client Message',
                'verbose_name_plural': 'Client Messages',
                'ordering': ['-time_stamp'],
            },
        ),
    ]