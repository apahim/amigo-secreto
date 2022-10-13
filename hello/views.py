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
    token = request.GET.get('token')
    queryset = Friends.objects.filter(token=token)
    if queryset.exists():
        user = queryset.values()
    else:
        user = None

    return render(
        request, "sorteio.html",
        {
            'token': token,
            'user': user,
        }
    )


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
