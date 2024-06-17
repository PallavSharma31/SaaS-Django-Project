from django.db import models

# Create your models here.

class PageVisit(models.Model):
    # primary key -> id will be give automatically if we don't specify
    """
    null=True means that the database will store NULL values in this column. This is particularly relevant for fields like 
    CharField and TextField.

    blank=True means that the field is allowed to be empty in forms. This affects Django's validation system.

    null=True, blank=True: The field is allowed to be empty both in the database (storing NULL) and in forms (form validation allows empty input). 
    This is common for optional fields
    """
    
    path=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
