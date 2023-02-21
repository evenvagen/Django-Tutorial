from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is a test.")


def home(request):
    return HttpResponse("You are home")