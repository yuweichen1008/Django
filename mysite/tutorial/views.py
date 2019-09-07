from django_tables2 import SingleTableView
from django.shortcuts import render
from .models import Person
from .tables import PersonTable

# Create your views here.
def index(request):
    return render(request, 'tutorial/index.html')

class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'tutorial/people.html'
    

def person_list(request):
    table = PersonTable(Person.objects.all())

    return render(request, "person_list.html", {
        "table": table
    })