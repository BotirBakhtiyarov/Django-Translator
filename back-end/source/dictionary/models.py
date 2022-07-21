from django.db import models

# Create your models here.
class dictionary(models.Model):

    chinese = models.CharField('Chinese',max_length=128)
    english = models.CharField('English',max_length=128)
