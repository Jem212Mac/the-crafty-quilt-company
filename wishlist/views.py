from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from .models import WishlistItem


@login_required
def wishlist(request):
    """ display the wishlist page """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishlistItem.objects.filter(user=user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ add a product to the wishlist"""
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    WishlistItem.objects.create(
        user=user,
        product=product
    )
    messages.success(
        request, f'{product.name} has been added to your Wishlist!')

    context = {
        'on_wishlist_page': True
    }

    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, item_id):
    """ remove product from the wishlist"""
    user = get_object_or_404(UserProfile, user=request.user)
    # get the item from the wishlist to be removed
    item = get_object_or_404(Product, pk=item_id)
    # check if the reuquested user owns the item to be removed
    WishlistItem.objects.filter(user=user, product=item).delete()
    messages.success(
            request,
            f'Successfully removed {item.name} from your wishlist!'
            )
    
    context = {
        'on_wishlist_page': True
    }
    
    return redirect('wishlist')