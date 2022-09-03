from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from django.template import  loader
from .models import Question
from django.http import Http404
# Create your views here.

def index(request):
    lates_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": lates_question_list
    }
    #return  HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)
def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return  render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas viendo lsos votos de  {question_id}")