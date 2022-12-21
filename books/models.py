from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from libraries.models import Library

# Create your models here.
User = get_user_model()

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom de l\'auteur')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

class Editor(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom de l\'éditeur')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Editeur'
        verbose_name_plural = 'Editeurs'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

class Collection(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom de la collection')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom de la catégorie')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Titre')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(verbose_name='Description')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Auteur')
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE, verbose_name='Editeur')
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Collection')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Catégorie')

    class Meta:
        verbose_name = 'Livre'
        verbose_name_plural = 'Livres'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

class Overdue(models.Model):
    reference = models.CharField(max_length=255, verbose_name='Référence')
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='En cours', verbose_name='Statut de l\'emprunt')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Emprunt'
        verbose_name_plural = 'Emprunts'

    def __str__(self):
        return self.book.title
