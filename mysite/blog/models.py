from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField(blank = True, null = True)