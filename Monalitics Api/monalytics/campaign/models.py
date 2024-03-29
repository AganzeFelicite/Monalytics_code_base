from django.utils import timezone
from django.db import models
import datetime


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    hash_tag = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    image_link = models.URLField()
    description = models.TextField()
    tiktok = models.BooleanField(default=False)
    instagram = models.BooleanField(default=False)
    facebook = models.BooleanField(default=False)
    twitter = models.BooleanField(default=False)
    youtube = models.BooleanField(default=False)
    linkedin = models.BooleanField(default=False)
    snapchat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_expired(self):
        return self.created_at + timezone.timedelta(days=self.time_limit) < timezone.now()

    def get_time_left(self):
        return self.created_at + timezone.timedelta(days=self.time_limit) - timezone.now()

    def get_time_left_in_days(self):
        today = datetime.date.today()

        end_datetime = self.created_at + \
            datetime.timedelta(days=self.time_limit)
        end_date = end_datetime.date()
        diff = end_date - today
        return diff.days
