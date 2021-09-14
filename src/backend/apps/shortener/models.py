from django.db import models
from django.utils import timezone

# Create your models here.

class URL(models.Model):
    label = models.CharField(null=True, blank=True, max_length=30)
    address = models.URLField()
    slug = models.SlugField(unique=True, max_length=8)
    visits = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(default=timezone.now)

    def increase_visits(self):
        self.visits += 1
        self.last_visit = timezone.now()
        self.save()

    def __str__(self):
        return self.label