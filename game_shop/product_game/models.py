from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CategoryGame(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Name Category: {self.name}'

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
        )
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(to='CategoryGame', on_delete=models.CASCADE)

    def __str__(self):
        return f'Game: {self.name} | Price Game {self.price} | Rating {self.rating}'