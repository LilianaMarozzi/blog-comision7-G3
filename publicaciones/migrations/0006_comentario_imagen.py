# Generated by Django 5.0 on 2023-12-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0005_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_publicaciones'),
        ),
    ]
