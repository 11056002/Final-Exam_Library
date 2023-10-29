from django.contrib import admin
from .models import Publisher, Book1, Author, LmssUser

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'addr')  # 调整列表显示顺序

class Autho1rAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_img', 'sex', 'age', 'tel')  # 调整列表显示顺序

class Book1Admin(admin.ModelAdmin):
    list_display = ('name', 'book_img', 'book_con', 'ISBN', 'translator', 'date', 'publisher', 'status')  # 调整列表显示顺序

class LmssUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'password')  # 调整列表显示顺序

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, Autho1rAdmin)
admin.site.register(Book1, Book1Admin)
admin.site.register(LmssUser, LmssUserAdmin)
