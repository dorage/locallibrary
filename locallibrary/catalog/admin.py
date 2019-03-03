from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Author)
class BookInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('id', 'status', 'due_back')

    fieldsets = (
        (None, {
            'fields' : ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields' : ('status', 'due_back')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)

