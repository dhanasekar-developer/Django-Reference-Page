from django.db import models

# Create your models here.
class Employee(models.Model):
    empcode = models.CharField(max_length=100),
    empname = models.IntegerField(),
    dateofjoin = models.DateField(),
    
    def __str__(self) -> str:
        return self.empname