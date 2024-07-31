from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from .models import Review


def review(request):
    """ display the product review page """
    user = get_object_or_404(UserProfile, user=request.user)
    review = Review.objects.filter(user=user)
    template = 'reviews/product_review.html'
    context = {
        'review': review,
    }

    return render(request, template, context)