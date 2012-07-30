from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def alt(request):
    return render(request, 'alt.html')
