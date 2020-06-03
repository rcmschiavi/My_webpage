from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from my_webpage import settings
import os


def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print("HTTP")
    else:
        ip = request.META.get('REMOTE_ADDR')
        print("REMOTE")
    print(ip)
    return render(request, 'index.html')

def resume(request):
    with open(os.path.join(settings.BASE_DIR, 'template/static/files/resume.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=resume.pdf'
        return response