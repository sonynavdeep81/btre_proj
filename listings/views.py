from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator


def listings(request):
    listngs = Listing.objects.all()
    paginator = Paginator(listngs, 3)
    # will return None for first time but paginator class handles it and assign page=1 for first time
    page = request.GET.get('page')
    listings_page = paginator.get_page(page)

    context = {
        'listings': listings_page
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listings = Listing.objects.filter(id=listing_id)
    context = {
        'listings': listings
    }
    return render(request, 'listings/listing.html', context)
