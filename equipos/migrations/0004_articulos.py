# Generated by Django 4.2.7 on 2023-11-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0003_alter_referentes_apellido'),
    ]

    operations = [
        migrations.CreateModel(
            name='articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('mensaje', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
