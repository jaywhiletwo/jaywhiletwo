from django.shortcuts import render_to_response

from .models import Post


def blog(request, post_slug=None):
    posts = Post.objects.all()
    post = Post.objects.get(slug=post_slug) if post_slug else Post.objects.first()

    return render_to_response('blog/blog.html', {
        'posts': posts,
        'post': post,
    })
