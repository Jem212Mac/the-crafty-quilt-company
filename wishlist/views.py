from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')

