from django.shortcuts import render


def test404(request):
    return render(request, "404.html")


def home(request):
    return render(request, "home/home.html")
