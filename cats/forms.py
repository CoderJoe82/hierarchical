from django.forms import modelform_factory
from cats.models import Cat

AddCatForm = modelform_factory(Cat, exclude=[])