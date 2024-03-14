from django.db.models.signals import post_save
from .models import TelephoneNumberCatalogue, TelephoneNumbers
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import pandas as pd

@receiver(post_save, sender=TelephoneNumberCatalogue)
def telephoneNumberCatalogue_post_save(sender, instance, **kwargs):
    df = pd.read_excel(instance.ods_file, engine="odf")
        
    for index, row in df.iterrows():
        try:
            t = TelephoneNumbers.objects.get(first_name=row['first name'], 
                                            last_name=row['last name'], 
                                                telephone_number=row['telephone number'])
        except:
            try:
                t = TelephoneNumbers.objects.create(first_name=row['first name'], 
                                                last_name=row['last name'], 
                                                    telephone_number=row['telephone number'])
                t.save()
            except:
                raise ValidationError('The file you tried to submit is not the appropriate')