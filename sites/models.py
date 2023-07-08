from django.db import models
from django.apps import apps
from django.urls import reverse

class Site(models.Model):
    region = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    availability_during_week = models.CharField(max_length=255)
    number_of_times_visited = models.PositiveIntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class SiteImage(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sites/', blank='True')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('site_image_detail', kwargs={'pk': str(self.pk)})

class SiteActivity(models.Model):
    name = models.CharField(max_length=255)
    charges = models.DecimalField(max_digits=9, decimal_places=2)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='site_activity_set')

    def __str__(self):
        return self.name


class Eatery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    number_of_times_visited = models.PositiveIntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='eateries_set')

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    eatery = models.ForeignKey(Eatery, on_delete=models.CASCADE, related_name='menu')
    category = models.CharField(max_length=255)
    meal_name = models.CharField(max_length=255)
    charges = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.meal_name


class EateryImage(models.Model):
    eatery = models.ForeignKey(Eatery, on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='eateries/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('eatery_image_detail', kwargs={'pk': str(self.pk)})
