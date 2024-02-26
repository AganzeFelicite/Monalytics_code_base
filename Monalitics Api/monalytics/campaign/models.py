from datetime import timezone
from django.db import models


class Campaign(models.Model):
    title = models.CharField(max_length=100)
    hash_tag = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    image_link = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_expired(self):
        return self.created_at + timezone.timedelta(days=self.time_limit) < timezone.now()

    def get_time_left(self):
        return self.created_at + timezone.timedelta(days=self.time_limit) - timezone.now()

    def get_time_left_in_days(self):
        return self.get_time_left().days
