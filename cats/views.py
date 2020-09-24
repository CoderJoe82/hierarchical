from django.shortcuts import render, redirect
from cats.models import Cat
from cats.forms import AddCatForm
# Create your views here.
def home(request):
    return render(request, 'home.html', {'nodes': Cat.objects.all()})

def add_cats(request):
    if request.method == 'POST':
        form = AddCatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddCatForm()
    return render(request, 'generic_form.html', {'form': form})