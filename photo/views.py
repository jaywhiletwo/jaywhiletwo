from django.shortcuts import render_to_response

from .models import Gallery


def image(request):
    return render_to_response('photo/image.html', {})


def image_set(request, gallery_slug=None):
    galleries = Gallery.objects.all()
    gallery = Gallery.objects.get(slug=gallery_slug) if gallery_slug else Gallery.objects.first()

    return render_to_response('photo/image_set.html', {
        'galleries': galleries,
        'gallery': gallery,
    })
