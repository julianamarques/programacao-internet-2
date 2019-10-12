# Generated by Django 2.2.6 on 2019-10-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('release_date', models.CharField(blank=True, default='', max_length=255)),
                ('game_category', models.CharField(blank=True, max_length=255, null=True)),
                ('played', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
                'ordering': ('name',),
            },
        ),
    ]
