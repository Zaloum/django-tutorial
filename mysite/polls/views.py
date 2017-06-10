from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Choice, Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list' : latest_question_list }    
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', { 'question' : question })

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question' : question, 
            'error_message' : "You didn't select a choice.", 
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with 
        # POST data. This prevents data from being posted twice if a user hits the 
        # back button.
        # reverse() helps avoid having to hardcode a URL in the view function
        # here it will return a string like '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

def results(request, question_id):
    # This is almost the exact same as detail(). The only difference is the template name. 
    # We'll fix this redundancy later.
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', { 'question' : question })
