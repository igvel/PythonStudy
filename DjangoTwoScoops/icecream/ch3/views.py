# Create your views here.
import datetime
from django.utils import timezone
from django.http import HttpResponse, Http404


def hello(request):
    return HttpResponse("Hello, world!")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = timezone.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
