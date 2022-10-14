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
    test = request.GET.get('test')
    try:
        user = Friends.objects.get(token=token)
        if user.friend is None:
            friend = Friends.objects.filter(
                available=True
            ).exclude(
                token=token
            ).exclude(
                available=False
            ).order_by('?').first()

            user.friend = friend.token
            user.save()

            friend.available = False
            friend.save()

            friend_name = friend.name
        else:
            friend = Friends.objects.get(token=user.friend)
            friend_name = friend.name
            # friend_name = None

    except Exception:
        user = None
        friend_name = None

    return render(
        request, "sorteio.html",
        {
            'token': token,
            'user': user,
            'friend': friend_name,
        }
    )


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
