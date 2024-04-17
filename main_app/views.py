from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, FavoriteFood
from .forms import GrabForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finchs_index(request):
    finchs = Finch.objects.all()
    return render(request, 'main_app/index.html', {
        'finchs': finchs
    })

def finchs_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.food.all().values_list('id')
    not_have_fav_food = FavoriteFood.objects.exclude(id__in=id_list)
    grab_form = GrabForm()
    return render(request, 'main_app/detail.html', {
        'finch': finch,
        'grab_form': grab_form,
        'favoritefood': not_have_fav_food,
    })

def add_grabbeditem(request, finch_id):
    form = GrabForm(request.POST)
    if form.is_valid():
        new_grabbeditem = form.save(commit=False)
        new_grabbeditem.finch_id = finch_id
        new_grabbeditem.save()
    return redirect('detail', finch_id=finch_id)

def fav_foods_index(request):
    favoritefood_list = FavoriteFood.objects.all()
    return render(request, 'main_app/favoritefood_list.html', {
        'favoritefood_list': favoritefood_list
    })

def assoc_favoritefood(request, finch_id, favoritefood_id):
    Finch.objects.get(id=finch_id).food.add(favoritefood_id)
    print(favoritefood_id)
    print(FavoriteFood.get(favoritefood_id))
    return redirect('detail', finch_id=finch_id)

def rm_assoc_favoritefood(request, finch_id, favoritefood_id):
    Finch.objects.get(id=finch_id).food.remove(favoritefood_id)
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finchs'

class FoodList(ListView):
    model = FavoriteFood

class FoodDetail(DetailView):
    model = FavoriteFood

class FoodCreate(CreateView):
    model = FavoriteFood
    fields = '__all__'

class FoodUpdate(UpdateView):
    model = FavoriteFood
    fields = ['description', 'cost']

class FoodDelete(DeleteView):
    model = FavoriteFood
    success_url = '/favoritefoods'