from django.db import models

class Feedback(models.Model):
 
    username = models.CharField(max_length=120)
    email= models.TextField(blank=True, null=True)
    feedback=models.TextField(blank=False, null=False)
    rating=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    
# Create your models here.
