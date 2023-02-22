from django.shortcuts import render
from django.http import HttpResponse
from realtor.models import Realtor
from listings.models import Listing

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }    
    return render(request, 'pages/index.html',context)


def about(request):
    realtors = Realtor.objects.filter(is_mvp=True)
    team = Realtor.objects.all()
    print(team)
    context = {
        'team':team,
        'realtors':realtors
    }
    return render(request, 'pages/about.html',context)
