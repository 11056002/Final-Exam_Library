"""
URL configuration for Mid-Exam_Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as mv
from library import views as lib
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.homepage, name="homepage"),
    path('default/', mv.showbook, name='default'),  
    path('book/', mv.showbook, name='show_book'),  
    path('publisher/', mv.showpublisher, name='show_publisher'), 
    path('author/', mv.showauthor, name='show_author'),  
    path('book/<str:book_name>/', mv.showbook, name='show_book_detail'),  
    path('publisher/<str:publisher_name>/', mv.showpublisher, name='show_publisher_detail'),  
    path('author/<str:author_name>/', mv.showauthor, name='show_author_detail'),  
    path('search_books/', mv.search_books, name='search_books')
]

