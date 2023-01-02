from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from djgeojson.fields import PointField

User = get_user_model()

class Library(models.Model):
    geom = PointField(blank = True, null=True)
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom de la librairie')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Adresse')
    city = models.CharField(max_length=255, verbose_name='Ville')
    postal_code = models.CharField(max_length=255, verbose_name='Code postal')
    statut = models.CharField(max_length=255, default='Actif', verbose_name='Statut de la librairie')
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

class Bookseller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Libraire'
        verbose_name_plural = 'Libraires'
        ordering = ['-created_at']

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
            
            super().save(*args, **kwargs)
