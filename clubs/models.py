from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from libraries.models import Library
from books.models import Book

User = get_user_model()

class Club(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom du club')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Description du club')
    capacity = models.PositiveIntegerField(verbose_name='Capacité du club')
    library = models.ForeignKey(Library, on_delete=models.CASCADE, verbose_name='Bibliothèque')
    books = models.ManyToManyField(Book, verbose_name='Livres')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super().save(*args, **kwargs)
    
class Session(models.Model):
    date = models.DateField(verbose_name='Date de la session')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name='Club')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'
        ordering = ['-created_at']

    def __str__(self):
        return self.date

    def save(self, *args, **kwargs):

        self.slug = slugify(self.date)

        super().save(*args, **kwargs)

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Utilisateur')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name='Club')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Membre'
        verbose_name_plural = 'Membres'
        ordering = ['-created_at']

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):

        self.slug = slugify(self.user)

        super().save(*args, **kwargs)

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Utilisateur')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='Session')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'
        ordering = ['-created_at']

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):

        self.slug = slugify(self.user)

        super().save(*args, **kwargs)

