# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genre(models.Model):
    """
    Model representing a book genre (Science Fiction, Biography, etc)
    """

    name = models.CharField(max_length = 200, help_text = "Enter a book genre (e.g. Science Fiction, French Poetry, etc.)")

    def __str__(self):
        """
        String representing the model object (in Admin site, etc.)
        """

        return self.name

class Language(models.Model):
    """
    Model representing a language a book is written in
    """

    name = models.CharField(max_length = 200, help_text = "Enter a book's language (English, Latin, etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book (but not a specific copy)
    """

    title = models.CharField(max_length = 200)
    author = models.ForeignKey("Author", on_delete = models.SET_NULL, null=True)
    summary = models.TextField(max_length = 1000, help_text = "Enter a brief description of the book.")
    isbn = models.CharField(max_length = 13, help_text = "13 Character <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>")
    genre = models.ManyToManyField(Genre, help_text = "Enter a genre for this book.")
    language = models.ForeignKey("Language", on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url of a particular book instance
        """

        return reverse("book detail", args=[str(self.id)])

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book
    """

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "Unique ID for this book across the entire library.")
    book = models.ForeignKey("Book", on_delete = models.SET_NULL, null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True, blank = True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On Loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default = "m", help_text = "Current status of a particular book.")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return "%s (%s)" % (self.id, self.book.title)

class Author(models.Model):
    """
    Model representing an Author
    """

    first_name = models.CharField(max_length = 200, help_text = "Author's first name.")
    last_name = models.CharField(max_length = 200, help_text = "Author's last name.")
    date_of_birth = models.DateField(null = True, blank = True)
    date_of_death = models.DateField("Died", null = True, blank = True)

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)
