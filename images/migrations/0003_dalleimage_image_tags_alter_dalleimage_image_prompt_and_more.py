# Generated by Django 5.0.2 on 2024-02-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_dalleimage_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dalleimage',
            name='image_tags',
            field=models.CharField(default='na', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dalleimage',
            name='image_prompt',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='dalleimage',
            name='image_url',
            field=models.URLField(max_length=1000),
        ),
    ]
