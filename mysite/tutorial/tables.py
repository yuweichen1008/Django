# https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html
import django_tables2 as tables
from .models import Person
data = [
    {"name": "Bradley"},
    {"name": "Stevie"},
]

class NameTable(tables.Table):
    name = tables.Column()

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("full name","first_name", "last_name","birth_date")