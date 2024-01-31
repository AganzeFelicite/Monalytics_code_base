# from django.contrib.auth.backends import BaseBackend
# from .models import Company


# class CompanyAuthenticationBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None):
#         try:
#             company = Company.objects.get(email=email)
#         except Company.DoesNotExist:
#             return None

#         if company.check_password(password):
#             return company

#         return None

#     def get_user(self, user_id):
#         try:
#             return Company.objects.get(pk=user_id)
#         except Company.DoesNotExist:
#             return None
