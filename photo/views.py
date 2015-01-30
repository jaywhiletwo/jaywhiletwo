from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from .models import Gallery, Image


def image_set(request, gallery_slug=None):
    message = ''
    if request.method == 'POST':
        delete_code = request.POST.get('delete_code')
        delete_image = request.POST.get('delete_image')
        if delete_code != '2016186099':
            message = "Incorrect delete code (hint: it's Jeff's phone number)"
        else:
            image = Image.objects.get(id=delete_image)
            image.deleted = True
            image.save()
            message = "Image deleted."

    galleries = Gallery.objects.all().order_by('display_name')

    if gallery_slug == 'deleted':
        image_queryset = Image.objects.filter(deleted=True)
    else:
        gallery = Gallery.objects.get(dir_name=gallery_slug) if gallery_slug else Gallery.objects.first()
        image_queryset = gallery.image_set.filter(deleted=False)

    p = Paginator(image_queryset, 20)

    page = request.GET.get('page')

    try:
        images = p.page(page)
    except PageNotAnInteger:
        images = p.page(1)
    except EmptyPage:
        images = p.page(p.num_pages)

    return render_to_response('photo/image_set.html', {
            'galleries': galleries,
            'images': images,
            'message': message,
        }, 
        context_instance=RequestContext(request)
    )
