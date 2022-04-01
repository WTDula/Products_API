from django.db import models

# Create your models here.
class Review(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    RATINGS_CHOICES = [
        (ONE, '1 (worst)'),
        (TWO, '2'),
        (THREE, '3 (indifferent)'),
        (FOUR, '4'),
        (FIVE, '5 (best)')
    ]
    rating = models.IntegerField(max_length=1, choices=RATINGS_CHOICES, default=THREE)
    foreign_key = models.IntegerField(max_length=4)
    description = models.CharField(max_length=255)
