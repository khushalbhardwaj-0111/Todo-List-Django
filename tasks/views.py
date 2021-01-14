from django.shortcuts import render, HttpResponse
from .forms import TodoForm
from .models import todo

# Create your views here.
def app(request):
    context = {
        'form': TodoForm,
        'todos': todo.objects.all()
    }
    return render(request, 'main.html', context)