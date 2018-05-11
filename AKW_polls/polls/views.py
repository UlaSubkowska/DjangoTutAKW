from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.


def index(request):
    return render(request, 'polls/index.html')


#widok za pomoca przycisku nastepne pytanie przekierowuje tak daleko po id az,
#id jest wieksze niz to istniejące, wtedy widok wylapuje wyjątek i zwraca templatke
#z wynikami
def detail(request, question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        all_questions = Question.objects.order_by('quest_number')
        context = {'all_questions': all_questions, }
        return render(request, 'polls/results.html', context)
    return render(request, 'polls/detail.html', {'question':question, 'question_id':question_id})


#tymczasowo nic nie robi
def results(request):
    all_questions=Question.objects.order_by('quest_number')
    context={'all_questions':all_questions,}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls:detail.html', {'question':question, 'error_message': "gówno",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        next_quest=question_id+1
        return HttpResponseRedirect(reverse('polls:detail', args=(next_quest,)))

