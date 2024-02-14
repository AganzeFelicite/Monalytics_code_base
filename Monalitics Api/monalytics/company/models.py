from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password


"""
this is a class that defines a company
note that some fields will be added later
"""


class SocialMediaAccount(models.Model):
    social_media_image = models.ImageField(
        upload_to='social_media', null=True, default='null')
    account_link = models.CharField(max_length=230)
    social_media_type = models.CharField(max_length=230)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='social_media_accounts')

    def __str__(self):
        return self.account_link

    class Meta:
        verbose_name_plural = "Social Media Accounts"


class Competitor(models.Model):
    '''
    this class defines a competitor
    '''
    competitor_name = models.CharField(max_length=230)
    competitor_image = models.ImageField(
        upload_to='competitors', null=True, default='null')
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='competitors')
    competitor_info = models.CharField(max_length=230)


class Company(models.Model):
    """
    this class defines a company
    """
    company_image = models.ImageField(
        upload_to='companies', null=True, default='null')
    company_name = models.CharField(max_length=230)
    email = models.CharField(max_length=230)
    sector = models.CharField(max_length=230)
    password = models.CharField(max_length=230)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    logged_in = models.BooleanField(default=False)
    country = models.CharField(max_length=230, default="Rwanda")

    city = models.CharField(max_length=230, default="Kigali")

    def __str__(self):
        return self.company_name

    def addSocialMediaAccount(self, account_link, social_media_type):
        account = SocialMediaAccount.objects.create(
            account_link=account_link, social_media_type=social_media_type, company=self)
        # self.social_media_accounts.append(account)
        return account

    def deleteSocialMediaAccount(self, account):
        account.delete()

    def addCompetitor(self, competitor_name, competitor_info):
        competitor = Competitor.objects.create(
            competitor_name=competitor_name, competitor_info=competitor_info, company=self)
        return competitor

    class Meta:
        verbose_name_plural = "Companies"

    def authenticate(self, password):
        is_password_correct = check_password(password, self.password)
        if is_password_correct:
            self.logged_in = True
            return self
        return None
