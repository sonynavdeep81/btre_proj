from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing


def listings(request):
    queryset = Listing.objects.all()
    context = {
        'listings': queryset
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listings = Listing.objects.filter(id=listing_id)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listing.html', context)
