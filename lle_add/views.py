from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from lle_add.forms import PlaceSearchForm
from lle_add.forms import PlaceAddForm
from .services import get_places

def search_place(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
    
        # Create a form instance and populate it with data from the request (binding):
        form = PlaceSearchForm(request.POST)

        if form.is_valid():
            search = form.cleaned_data['search']
            places = get_places(search)

            context = {
                'form': form,
                'places': places,
            }

        return render(request, 'add/search.html', context)

        # Check if the form is valid:

    # If this is a GET (or any other method) create the default form.
    else:
        form = PlaceSearchForm()

        context = {
            'form': form,
        }

        return render(request, 'add/search.html', context)

def add_place(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
    
        # Create a form instance and populate it with data from the request (binding):
        form = PlaceAddForm(request.POST)

        if form.is_valid():
            placedata = form.cleaned_data
            
            context = {
                'form': form,
                'places': placedata,
            }

        return render(request, 'add/place.html', context)

        # Check if the form is valid:

    # If this is a GET (or any other method) create the default form.
    else:
        form = PlaceAddForm(request.GET)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']

            context = {
                'form': form,
                'name': name,
                'address': address,
            }

        return render(request, 'add/place.html', context)

