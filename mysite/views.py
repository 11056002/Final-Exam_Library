from django.shortcuts import render, redirect
from mysite.models import Book1, Publisher, Author
def homepage(request):
    books = Book1.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'index.html', locals())
def showbook(request, book_name="None"):
    try:
        book = Book1.objects.get(name=book_name)
        return render(request, 'book.html', {'book': book})
    except Book1.DoesNotExist:
        return redirect("/")  # 書本不存在，重定向到首頁

def showauthor(request, author_name="None"):
    try:
        author = Author.objects.get(name=author_name)
        return render(request, 'author.html', {'author': author})
    except Author.DoesNotExist:
        return redirect("/")  # 作者不存在，重定向到首頁

def showpublisher(request, publisher_name="None"):
    try:
        publisher = Publisher.objects.get(name=publisher_name)
        return render(request, 'publisher.html', {'publisher': publisher})
    except Publisher.DoesNotExist:
        return redirect("/")  # 出版商不存在，重定向到首頁
