# Generated by Django 3.2.6 on 2021-08-20 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowertypes', '0004_assortedflowers_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assortedflowers',
            old_name='discount',
            new_name='sale',
        ),
    ]
