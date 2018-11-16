from django.db import models

# Create your models here.


UPLOAD_TO_PATH = 'uploads/%Y/%m/%d/'


class Project(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=UPLOAD_TO_PATH, blank=True)
    headline = models.CharField(max_length=150, blank=True)
    interest_areas = models.CharField(max_length=100, blank=True)
    regions = models.CharField(max_length=100, blank=True)
    foundation = models.CharField(max_length=100, blank=True)
    employees = models.CharField(max_length=100, blank=True)
    units = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    published = models.BooleanField(default=False)

    email = models.EmailField()
    cnpj = models.CharField(max_length=100, blank=True)
    owner_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.pk} {self.name}'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=UPLOAD_TO_PATH)
