from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from cats.models import Cat

# Register your models here.
admin.site.register(Cat, DraggableMPTTAdmin)