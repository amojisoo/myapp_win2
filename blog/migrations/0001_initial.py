# Generated by Django 2.0.7 on 2018-07-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('release_data', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]