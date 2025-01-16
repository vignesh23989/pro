from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')]
def calculateAge(birthDate):
        from datetime import date
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))    
        return age

class Department(models.Model):
    name =models.CharField(max_length=50, verbose_name="Department Name")
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
         return self.name
    
    class Meta:
        verbose_name_plural  = 'Departments'

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    register_no = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES)
    DOB = models.DateField()
    phone = models.CharField(max_length=12, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    department = models.ForeignKey(Department, verbose_name="Department", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.first_name
        #  return self.first_name + " " + self.last_name if self.last_name else self.first_name
    
    class Meta:
        ordering = ["first_name"]
    
    
    def clean(self):
        if self.age:
            if self.age <=18:
                raise ValidationError("Age must be grater than or equal to 18")
    def save(self, *args, **kwargs):
        if self.DOB:
            self.age = calculateAge(self.DOB)
        # self.clean()
        # if 'test' in self.email:
        #     self.email = self.email.replace("test", "gmail")
        super().save(*args, **kwargs)

