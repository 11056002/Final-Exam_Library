from django.contrib import admin
from .models import Publisher, Book1, Author, LmssUser

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'addr')  # 調整列表顯示順序

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_img', 'sex', 'age', 'tel')   # 調整列表顯示順序

class Book1Admin(admin.ModelAdmin):
    list_display = ('name', 'book_img', 'book_con1', 'book_con2', 'ISBN', 'translator', 'date', 'publisher', 'status')  # 調整列表顯示順序

class LmssUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'password')  # 調整列表顯示順序

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book1, Book1Admin)
admin.site.register(LmssUser, LmssUserAdmin)
