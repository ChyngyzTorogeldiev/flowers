# Generated by Django 3.2.6 on 2021-08-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowertypes', '0002_seasonflowers'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssortedFlowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='assorted')),
            ],
            options={
                'verbose_name': 'Ассорти букет',
                'verbose_name_plural': 'Ассорти букеты',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='rosesbouquets',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='roses'),
        ),
        migrations.AlterField(
            model_name='seasonflowers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='seasonal'),
        ),
    ]