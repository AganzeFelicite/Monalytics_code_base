from django.db import models
from company.models import SocialMediaAccount

# Create your models here.


class Influencer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sector = models.CharField(max_length=100)
    social_media = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    last_login_ip = models.GenericIPAddressField()

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'influencer'
        verbose_name = 'Influencer'
        verbose_name_plural = 'Influencers'
        ordering = ['full_name']

    def addSocialMediaAccount(self, account_link, social_media_type):
        account = SocialMediaAccount.objects.create(
            account_link=account_link, social_media_type=social_media_type, influencer=self)
        return account
