# Generated by Django 3.2.6 on 2021-08-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='homeflowers')),
            ],
            options={
                'verbose_name': 'Комнатные цветы и растения',
                'ordering': ['name'],
            },
        ),
    ]