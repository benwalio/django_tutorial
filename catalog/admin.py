# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Author, Genre, Language, Book, BookInstance
from django.contrib import admin

# Register your models here.

# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(Book)
# admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    extra = 0
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    extra = 0
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "id", "status")
    list_filter = ("status", "due_back")

    fieldsets = (
        (None, {
            "fields": ("book", "imprint", "id")
        }),
        ("Availability", {
            "fields": ("status", "due_back")
        }),
    )
