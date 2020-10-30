from .models import Bb, Rubric
from django.shortcuts import render


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {"bbs": bbs, "rubrics": rubrics}
    return render(request, 'board/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'board/by_rubric.html', context)
