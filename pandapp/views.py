from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from .models import TelephoneNumberCatalogue, TelephoneNumbers
from django.conf import settings
import pandas as pd
import os

# Create your views here.
class CatalogueView(ListView):
    template_name = 'pandapp/catalogue.html'
    context_object_name = 'all_telephone_numbers'
    def get_queryset(self):
        return TelephoneNumbers.objects.all()

class FileForm(CreateView):
    model = TelephoneNumberCatalogue
    fields = "__all__"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        try:
            path_file = os.path.join(settings.BASE_DIR, f"static/media/ods/{self.object.odt_file}")
            print(path_file)
            odt = TelephoneNumberCatalogue.objects.get(odt_file="ods/Untitled_1.ods")
            print(odt.odt_file)
            print("I found it")
        except:
            print("I did not find it")
        return super().form_valid(form)





# install pandas and odfpy
        