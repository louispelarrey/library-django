from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from djgeojson.fields import PointField

User = get_user_model()

class Library(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom de la librairie')
    description = models.TextField(verbose_name='Description de la librairie', blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    geom = PointField(blank = True, null=True)  
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Librairie'
        verbose_name_plural = 'Librairies'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super().save(*args, **kwargs)