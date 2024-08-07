from django.db import models


class Contact(models.Model):
    """
    Stores a 'contact us' request message.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact Us request from {self.name}"
