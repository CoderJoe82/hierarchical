from django.urls import path
from cats import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('generic_form.html', views.add_cats, name = 'addcat')
]