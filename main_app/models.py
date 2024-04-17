from django.db import models
from django.urls import reverse

# Create your models here.
class FavoriteFood(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('favoritefood_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    food = models.ManyToManyField(FavoriteFood)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
class GrabbedItem(models.Model):
    item = models.CharField(max_length=100)
    rarity = models.IntegerField(default=1)
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Item: {self.item} Rarity: {self.rarity}" 
    
    class Meta:
        ordering = ['-rarity']
