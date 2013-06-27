# Create your views here.
from django.shortcuts import render


def meta(request):
    context = {'path': request.path, 'meta': dict(request.META)}
    return render(request, 'meta.html', context)

