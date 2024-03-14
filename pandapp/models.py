from django.db import models
from django.urls import reverse

# Create your models here.
class TelephoneNumberCatalogue(models.Model):
    ods_file = models.FileField(upload_to="ods/", verbose_name="ods file", null=True)

    def get_absolute_url(self):
        return reverse("catalogue")

class TelephoneNumbers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    telephone_number = models.PositiveBigIntegerField()

    def __str__(self):
        return f"Telephone number of {self.first_name} {self.last_name}"
    