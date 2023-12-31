from django.shortcuts import render, redirect
from mysite.models import Book1, Publisher, Author

def homepage(request):
    selected_menu = request.GET.get('menu', 'default')  # 默認顯示書本
    if selected_menu == 'book':
        articles = Book1.objects.all()
    elif selected_menu == 'author':
        articles = Author.objects.all()
    elif selected_menu == 'publisher':
        articles = Publisher.objects.all()
    elif selected_menu == 'default':
        articles = Publisher.objects.all()
    else:
        return redirect("/")  # 處理無效的MENU選項，直接重定向到首頁
    return render(request, 'index.html', {'selected_menu': selected_menu, 'articles': articles})

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
    
    
def search_books(request):
    if 'keyword' in request.GET:
        search_query = request.GET.get('keyword', '')
        books = Book1.objects.filter(name__icontains=search_query)
        if not books:
            return render(request, 'book_search_results.html', {'no_result': True})
        else:
            return render(request, 'book_search_results.html', {'books': books,})
    else:
        return render(request, 'N.html')

def search_books(request):
    keyword = request.GET.get('keyword', '').strip()

    if not keyword:  # 如果關鍵字空的awa
        return render(request, 'search_book.html', {'empty': True})
    else:
        books = Book1.objects.filter(name__icontains=keyword)
        if not books: #如果沒有此書籍ouo
            return render(request, 'search_book.html', {'no_result': True, 'keyword': keyword})
        else:
            return render(request, 'search_book.html', {'books': books, 'keyword': keyword})
