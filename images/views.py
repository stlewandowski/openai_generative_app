from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DallEForm
import os
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.utils import timezone
from openai_helpers.openai_api import OpenaiAPI
from .models import DallEImage
from django.db.models import Max, Min


def index(request):
    form = DallEForm()
    items_per_page = request.GET.get('items_per_page', 6)
    images_list = DallEImage.objects.all()
    paginator = Paginator(images_list, items_per_page)
    page_number = int(request.GET.get('page')) if request.GET.get('page') else 1
    images = paginator.get_page(page_number)

    # Get the total number of pages
    num_pages = paginator.num_pages

    # Create a list of page numbers to display
    # This includes the first 2 pages, the last 2 pages, and the current page
    print(page_number)
    print(num_pages)
    start_page = max(1, page_number - 3)
    end_page = min(num_pages, page_number + 3)
    page_numbers = list(range(start_page, end_page + 1))

    print(page_numbers)
    context = {"images": images, 'form': form, 'items_per_page': items_per_page, 'page_numbers': page_numbers}
    return render(request, "index.html", context)


def all_details(request):
    images = DallEImage.objects.all()

    # Get the filter criteria from the GET request
    prompt = request.GET.get('prompt')
    tags = request.GET.get('tags')
    quality = request.GET.get('quality')
    style = request.GET.get('style')

    # Apply the filter criteria to the query
    if prompt:
        images = images.filter(image_prompt__icontains=prompt)
    if tags:
        images = images.filter(image_tags__icontains=tags)
    if quality:
        images = images.filter(image_quality=quality)
    if style:
        images = images.filter(image_style=style)

    return render(request, 'all_details.html', {'images': images})


def create(request):
    if request.method == 'POST':
        form = DallEForm(request.POST, request.FILES)
        if form.is_valid():
            prompt = form.cleaned_data['image_prompt']
            user = form.cleaned_data['image_user']
            model = form.cleaned_data['image_model']
            quality = form.cleaned_data['image_quality']
            style = form.cleaned_data['image_style']
            size = form.cleaned_data['image_size']
            number = form.cleaned_data['image_number']
            tags = form.cleaned_data['image_tags']

            # Send request to Dall-E 3 API
            api = OpenaiAPI()
            response = api.get_image(prompt, size, quality, style, user, number, model)

            # save image to media folder using azure settings in settings.py
            # save image from url
            image_response = requests.get(response)
            image_data = image_response.content

            image_path = default_storage.save('media/' + response.split('/')[-1], ContentFile(image_data))

            # Create and save DallEImage instance
            dalle_image = DallEImage(
                image=image_path,
                image_prompt=prompt,
                image_date=timezone.now(),
                image_model=model,
                image_quality=quality,
                image_style=style,
                image_user=user,
                image_size=size,
                image_url=response,
                image_tags=tags
            )
            dalle_image.save()
            # send the image path to the results page
            request.session['context_data'] = {"image_path": image_path}
            return redirect('results')
    else:
        form = DallEForm()

    return render(request, 'create.html', {'form': form})


def results(request):
    context = request.session.get('context_data')
    # select the correct image from the image_path in the context data
    image_path = context['image_path']
    dalle_image = DallEImage.objects.get(image=image_path)

    # Pass the DallEImage instance to the template
    context = {
        "dalle_image": dalle_image,
    }

    return render(request, "results.html", context)


def img(request, img_id):
    # get the image from the database
    dalle_image = DallEImage.objects.get(image_id=img_id)

    # get the previous and next images
    prev_image = DallEImage.objects.filter(image_id__lt=img_id).order_by('-image_id').first()
    next_image = DallEImage.objects.filter(image_id__gt=img_id).order_by('image_id').first()

    context = {
        "dalle_image": dalle_image,
        "prev_image": prev_image,
        "next_image": next_image,
    }
    return render(request, "img.html", context)


def about(request):
    context = {"images": [], "tags": [], "prompts": [], "form": None, "results": [], "testval": "testval_about"}
    return render(request, "about.html", context)
