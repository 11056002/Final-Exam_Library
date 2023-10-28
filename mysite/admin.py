from django.contrib import admin
from mysite.models import Post, Publisher, Book, Author, LmsUser

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'addr')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'age', 'tel')

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'img_and_con', 'ISBN', 'translator', 'date', 'publisher','status')

class LmsUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'mobile')

admin.site.register(Post, PostAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(LmsUser, LmsUserAdmin)

