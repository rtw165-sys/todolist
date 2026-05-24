from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("<h11>Hello Django!</h1>")


def profile(request):
    context = {
        "name": "Daisy",
        "age": 50,
        "height": 150,
        "weight": 60,
    }

    return JsonResponse(context)
