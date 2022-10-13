from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Friends

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    para = request.GET.get('message')
    return render(request, "index.html", {'para': para})


def sorteio(request):
    error = None
    token = request.GET.get('token')
    user = Friends.objects.filter(token=token)
    if user is None:
        error = "Usuário não encontrado. Entre em contato com o admin."

    return render(request, "sorteio.html", {'token': token, 'error': error})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
