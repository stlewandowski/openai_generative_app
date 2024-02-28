from django.db import models


# Create your models here.
# TODO: need to update the fields for this model and activate model in settings.py
class DallEImage(models.Model):
    MODEL_CHOICES = [
        ('dall-e-2', 'dall-e-2'),
        ('dall-e-3', 'dall-e-3'),
    ]
    QUALITY_CHOICES = [
        ('hd', 'hd'),
        ('standard', 'standard'),
    ]
    STYLE_CHOICES = [
        ('vivid', 'vivid'),
        ('natural', 'natural'),
    ]
    SIZE_CHOICES = [
        ('256x256', '256x256'),
        ('512x512', '512x512'),
        ('1024x1024', '1024x1024'),
        ('1024x1792', '1024x1792'),
        ('1792x1024', '1792x1024'),
    ]

    image = models.ImageField(upload_to='media/', max_length=1000)
    image_id = models.AutoField(primary_key=True)
    image_prompt = models.CharField(max_length=1000)
    image_date = models.DateTimeField('date published')
    image_model = models.CharField(max_length=255, choices=MODEL_CHOICES)
    image_quality = models.CharField(max_length=255, choices=QUALITY_CHOICES)
    image_style = models.CharField(max_length=255, choices=STYLE_CHOICES)
    image_user = models.CharField(max_length=255)
    image_tags = models.CharField(max_length=255)
    image_size = models.CharField(max_length=255, choices=SIZE_CHOICES)
    image_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.image_prompt
