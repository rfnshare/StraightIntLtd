from django.db import models

# Create your models here.

from django.db import models


class Continent(models.Model):
    continent_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.continent_name


class Country(models.Model):
    country_name = models.CharField(max_length=10, blank=True, null=True)
    continent_name = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_name = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.state_name


class MyCustomModal(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
