from django.shortcuts import render
from django.http import HttpResponse
from realtor.models import Realtor
from listings.models import Listing
from listings.choices import bedrooms, prices, states


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
        'bedrooms': bedrooms,
        'prices': prices,
        'states': states
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.filter(is_mvp=True)
    team = Realtor.objects.all()
    print(team)
    context = {
        'team': team,
        'realtors': realtors
    }
    return render(request, 'pages/about.html', context)


def search(request):
    listings = Listing.objects.all()
    if request.GET.get('city'):
        city = request.GET.get('city')
        listings = listings.filter(city=city)

    if request.GET.get('bedrooms'):
        bdrooms = request.GET.get('bedrooms')
        listings = listings.filter(bedrooms__gte=bdrooms)

    if request.GET.get('state'):
        state = request.GET.get('state')
        listings = listings.filter(state=state)

    if request.GET.get('price'):
        price = request.GET.get('price')
        listings = listings.filter(price__gt=price)

    if request.GET.get('keywords'):
        keywords = request.GET.get('keywords')
        listings = listings.filter(description__icontains=keywords)

    context = {
        'listings': listings,
        'bedrooms': bedrooms,
        'prices': prices,
        'states': states,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
