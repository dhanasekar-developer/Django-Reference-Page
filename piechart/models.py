from django.db import models

# Create your models here.

class Chart(models.Model):
    category = models.CharField(max_length=100,null=False,blank=False)
    num_of_product = models.IntegerField()

    def __str__(self):
        return f'{self.category} - {self.num_of_product}'