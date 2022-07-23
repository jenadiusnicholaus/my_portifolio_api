from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import FileField, ImageField


class Technologies(models.Model):
    name=models.CharField(max_length=300, null=True, blank=False)
    class Meta:
        verbose_name_plural = 'Tech Stacks'
    def __str__(self):
        return f'{self.name}'

class Projects(models.Model):
    title = models.CharField(max_length= 400, null = True , blank=False)
    description = models.TextField(null=True)
    featured =models.CharField(max_length=400,null=True, blank=False)
    image=models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    techonologies = models.ManyToManyField(Technologies)
    link_to_live_version = models.URLField(null=True, blank=True)
    link_to_dource = models.URLField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Projects list'
    def __str__(self):
        return f'{self.title}'
