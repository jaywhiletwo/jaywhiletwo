from django.shortcuts import render_to_response

from .models import Post


def list(request):
    posts = Post.objects.all()
    return render_to_response('blog/list.html', {
        'posts': posts,
    })
