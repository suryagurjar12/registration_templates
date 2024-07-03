from django.db import models



# Create your models here.
class Registration(models.Model):   #model, forms.py ,serializers.py
    Name= models.CharField(max_length=50)
    Email= models.EmailField()
    Contact=models.IntegerField()
   
    