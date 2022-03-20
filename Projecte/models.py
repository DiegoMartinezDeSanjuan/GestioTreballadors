from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=30)
    init_date = models.DateField()

    def __str__(self):
        return str(self.name)
