from .models import Bb
from django.shortcuts import render


def index(request):
    bbs = Bb.objects.all()
    context = {"bbs": bbs}
    return render(request, 'board/index.html', context)
