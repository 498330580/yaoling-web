from django.shortcuts import render

# Create your views here.
from .models import *


def index(request):
    categorys = Category.objects.all()
    guides = Guide.objects.all()
    return render(request, 'gateway/index.html', locals())
