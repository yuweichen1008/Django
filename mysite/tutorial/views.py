from django.shortcuts import render
from django.views.generic import ListView
from .models import Person
# Create your views here.
def index(request):
    return render(request, 'tutorial/index.html')


class PersonListView(ListView):
    model = Person
    template_name = 'tutorial/people.html'