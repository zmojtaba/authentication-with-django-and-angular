# Generated by Django 4.1.5 on 2023-01-30 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_adress_extra_commnent'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='adress_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
