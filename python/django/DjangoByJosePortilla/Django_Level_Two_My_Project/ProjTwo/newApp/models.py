from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    user_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_email
