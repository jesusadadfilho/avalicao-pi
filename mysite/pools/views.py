from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from pools.models import *


def index(request):
    return render(request, 'index.html', {"questions": Question.objects.order_by('-pub_date')})


def exibir(request):
    return render(request, 'exibir.html')


def question(request, question_id):
    q = Question.objects.get(id=question_id)
    return render(request, 'question.html', {'question': q})


def results(request, question_id):
    q = Question.objects.get(id=question_id)
    a = 0
    for i in q.choices.all():
        a += i.votes
    return render(request, 'results.html', {'question': q, 'total': a})


def votes(request, question_id):
    q = Question.objects.get(id=question_id)
    return render(request, 'vote.html', {'question': q})

def votar(request, question_id, choice_id):
    q = Question.objects.get(id=question_id)
    a = q.choices.get(id = choice_id)
    a.votar()
    return (request)
