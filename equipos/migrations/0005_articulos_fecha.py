# Generated by Django 4.2.7 on 2023-11-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_articulos'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='fecha',
            field=models.DateField(max_length=20, null=True),
        ),
    ]
