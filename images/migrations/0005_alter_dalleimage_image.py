# Generated by Django 5.0.2 on 2024-02-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_dalleimage_image_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dalleimage',
            name='image',
            field=models.ImageField(max_length=1000, upload_to='media/'),
        ),
    ]