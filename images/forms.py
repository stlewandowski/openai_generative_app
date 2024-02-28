from django import forms
from .models import DallEImage


class DallEForm(forms.Form):
    image_prompt = forms.CharField(label="Prompt", max_length=1000, widget=forms.Textarea(attrs={'rows': 3, 'cols': 75}))
    image_tags = forms.CharField(label="Tags", max_length=255, widget=forms.TextInput(attrs={'size': '50'}))
    image_user = forms.CharField(label="User", max_length=255)
    image_model = forms.ChoiceField(label="Model", choices=DallEImage.MODEL_CHOICES, initial='dall-e-3')
    image_quality = forms.ChoiceField(label="Quality", choices=DallEImage.QUALITY_CHOICES, initial='hd')
    image_style = forms.ChoiceField(label="Style", choices=DallEImage.STYLE_CHOICES, initial='vivid')
    image_size = forms.ChoiceField(label="Size", choices=DallEImage.SIZE_CHOICES, initial='1792x1024')
    image_number = forms.IntegerField(label="Number", min_value=1, max_value=10, initial=1)
