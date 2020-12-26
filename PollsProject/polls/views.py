from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .form import PollForm
from .models import Poll


# Create your views here.
def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'home.html', context)


def create(request):
    poll = PollForm()
    if request.method == "POST":
        poll = PollForm(request.POST)
        if poll.is_valid():
            poll.save()
            return HttpResponseRedirect(reverse('polls:home'))

    context = {
        'poll': poll
    }
    return render(request, 'create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == "POST":
        selected_option = request.POST['poll']

        if selected_option == 'option1':
            poll.option1_count += 1

        elif selected_option == 'option2':
            poll.option2_count += 1

        elif selected_option == 'option3':
            poll.option3_count += 1

        else:
            return HttpResponse(400, "Invalid selection")

        poll.save()

        return HttpResponseRedirect(reverse('polls:home'))

    context = {
        'poll': poll
    }
    return render(request, 'vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'results.html', context)
