from django.contrib import admin
from .models import KYCdetails, Login, RateofInterest, abcacc
# Register your models here.

admin.site.register(Login)
admin.site.register(KYCdetails)
admin.site.register(RateofInterest)
admin.site.register(abcacc)