from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password


"""
this is a class that defines a company
note that some fields will be added later
"""


class Company(models.Model):
    """
    this class defines a company
    """
    company_name = models.CharField(max_length=230)
    email = models.CharField(max_length=230)
    sector = models.CharField(max_length=230)
    password = models.CharField(max_length=230)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Companies"

    def authenticate(self, password):
        is_password_correct = check_password(password, self.password)
        if is_password_correct:
            self.logged_in = True
            return self
        return None
