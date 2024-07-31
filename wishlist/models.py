from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from profiles.models import UserProfile


class WishlistItem(models.Model):
    """ Wishlist model to store users favourite products """
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE,
        )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return the string """
        return f"Wishlist ({self.user})"