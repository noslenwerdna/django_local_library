from django.contrib import admin
from .models import Author, AuthorAdmin, Genre, Book, BookInstance, Language

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Language)
