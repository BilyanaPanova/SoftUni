from datetime import datetime, date

from django.db import models
from django.db.models.fields import URLField
from django.utils.timezone import now


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Department(models.Model):
    CITY_NAME_CHOICES = {
        'Sofia': 'Sofia',
        'Plovdiv': 'Plovdiv',
        'Burgas': 'Burgas',
        'Varna': 'Varna'
    }

    code = models.CharField(primary_key=True,
                            max_length=4,
                            unique=True)
    name = models.CharField(max_length=50,
                            unique=True)
    employees_count = models.PositiveIntegerField(default=1,
                                                  verbose_name="Employees Count")
    location = models.CharField(max_length=20,
                                null=True,
                                blank=True,
                                choices= CITY_NAME_CHOICES.items())
    last_edited_on = models.DateTimeField(auto_now=True,
                                          editable=False)


class Project(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)
    description = models.TextField(blank=True,
                                   null=True)
    budget = models.DecimalField(blank=True,
                                 null=True,
                                 decimal_places=2,
                                 max_digits=10)
    duration_in_days = models.PositiveIntegerField(blank=True,
                                                   null=True,
                                                   verbose_name="Duration in Days")
    estimated_hours = models.FloatField(blank=True,
                                        null=True,
                                        verbose_name="Estimated Hours")
    start_date = models.DateField(verbose_name="Start Date",
                                  blank=True,
                                  null=True,
                                  default=date.today())
    created_on = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    last_edited_on = models.DateTimeField(auto_now=True,
                                          editable=False)