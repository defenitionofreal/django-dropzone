from django.shortcuts import render
from .models import ImageDrop
from django.http import HttpResponse, JsonResponse


def index(request):
    images = ImageDrop.objects.all()
    context = {"images": images}
    return render(request, 'index.html', context)


def file_upload(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        ImageDrop.objects.create(image=my_file)
        return HttpResponse('Done')
    return JsonResponse({'post': 'false'})
