from django.db import models

# Create your models here.


class Project(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.pk} {self.name}'
