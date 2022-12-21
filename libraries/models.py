from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()

class Library(models.Model):
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