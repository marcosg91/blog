# Generated by Django 4.1.4 on 2022-12-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0002_alter_entrada_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]