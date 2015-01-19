from django.shortcuts import render



def image(request):
    return render(request, 'photo/show.html')


def image_set(request):
    return render(request, 'photo/show.html')
