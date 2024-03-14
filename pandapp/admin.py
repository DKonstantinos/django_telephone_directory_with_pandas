from django.contrib import admin
from .models import TelephoneNumberCatalogue, TelephoneNumbers

# Register your models here.
admin.site.register(TelephoneNumberCatalogue)
admin.site.register(TelephoneNumbers)