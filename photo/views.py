from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response

from .models import Gallery


def image_set(request, gallery_slug=None):
    galleries = Gallery.objects.all()
    gallery = Gallery.objects.get(dir_name=gallery_slug) if gallery_slug else Gallery.objects.first()

    p = Paginator(gallery.image_set.all(), 30)

    page = request.GET.get('page')

    try:
        images = p.page(page)
    except PageNotAnInteger:
        images = p.page(1)
    except EmptyPage:
        images = p.page(p.num_pages)

    return render_to_response('photo/image_set.html', {
        'galleries': galleries,
        'gallery': gallery,
        'images': images,
    })
