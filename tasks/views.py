from django.shortcuts import render, HttpResponse

# Create your views here.
def app(requests):
    return render(requests, 'main.html')