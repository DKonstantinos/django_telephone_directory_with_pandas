from django.urls import path
from . import views

urlpatterns = [
    path("catalogue/", views.CatalogueView.as_view(), name='catalogue'),
    path("submit/", views.FileForm.as_view(), name='submit_form'),
]
