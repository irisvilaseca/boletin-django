from django.db import models

# Create your models here.
class Registered(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField()
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    
    
    def _str_(self):
        return self.email