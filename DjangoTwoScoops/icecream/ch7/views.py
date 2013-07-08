# Create your views here.
from time import timezone
from django.shortcuts import render


def meta(request):
    context = {'path': request.path, 'meta': dict(request.META)}
    return render(request, 'meta.html', context)


def date(request, month, day):
    return render(request, 'date.html', {"month": month, "day": day, "message": "Long message with spaces!"})
