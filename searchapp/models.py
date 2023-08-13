from django.db import models
from django.contrib.auth.models import User


class SearchInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.TextField()
    search_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
