from django.db import models

# Create your models here.

class Framework(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    date_of_creation = models.DateField()

    def __str__(self):
        return self.name
