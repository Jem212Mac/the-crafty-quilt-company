from django.contrib import admin
from . models import WishlistItem


@admin.register(WishlistItem)
class WishlistAdmin(admin.ModelAdmin):
    """wishlist admin"""
    model = WishlistItem
    fields = ('user', 'product')
    list_display = ('user', 'product')