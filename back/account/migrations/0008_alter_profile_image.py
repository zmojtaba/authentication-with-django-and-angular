# Generated by Django 4.1.5 on 2023-01-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_adress_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
