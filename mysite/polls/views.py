from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def createq(request):
    try:
        text = request.POST['question']
    except KeyError:
        return render(request, "polls/error.html", {"message": "No question given"})
    if text == "":
        return render(request, "polls/error.html", {"message": "No question given"})
    else:
        question = Question(question_text=text, pub_date=timezone.now())
        question.save()
        return HttpResponseRedirect(reverse("polls:index"))
     
def deleteq(request, question_id):
    question = get_object_or_404(Question, pk=question_id) 
    question.delete()
    return HttpResponseRedirect(reverse("polls:index"))

def addOpt(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        choice = request.POST['option']
    except KeyError:
        return render(request, "polls/error.html", {"message": "No choice provided"})
    if choice == "":
        return render(request, "polls/error.html", {"message": "No choice provided"})
    else:
        question.choice_set.create(choice_text=choice)
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))