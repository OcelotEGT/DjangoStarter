"""Users models."""

#Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other information.
    """

    
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/picures',
         blank=True,
          null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns username."""
        return self.user.username
