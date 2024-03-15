from django.db import models
from category.models import Category
# Create your models here.


class CreateTaskModel(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField()
    date  =models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=0, choices=[(i, i) for i in range(9)])
    category = models.ForeignKey(Category,on_delete =models.CASCADE)
    status = models.BooleanField(default =False)
    
    def __str__(self) -> str:
        return self.title
    