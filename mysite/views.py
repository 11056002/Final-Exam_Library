from django.shortcuts import render
from mysite.models import Post, Book,Publisher,Author
from datetime import datetime
from django.shortcuts import redirect

def homepage(request):
    selected_menu = request.GET.get('menu', 'book')  # 默认显示书本
    if selected_menu == 'book':
        articles = Book.objects.all()
    elif selected_menu == 'author':
        articles = Author.objects.all()
    elif selected_menu == 'publisher':
        articles = Publisher.objects.all()
    else:
        articles = []  # 处理无效的MENU选项
    return render(request, 'index.html', {'selected_menu': selected_menu, 'articles': articles})

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
#書本
def showbook(request, book_name="None"):
    try:
        book = Book.objects.get(name=book_name)
        if book:
            return render(request, 'book.html', {'book': book})
        else:
            return redirect("/")
    except Book.DoesNotExist:
        return redirect("/")
#作者
def showauthor(request, author_name="None"):
    try:
        author = Author.objects.get(name=author_name)
        if author:
            return render(request, 'author.html', {'author': author})
        else:
            return redirect("/")
    except Author.DoesNotExist:
        return redirect("/")

#出版商
def showpublisher(request, publisher_name="None"):
    try:
        publisher = Publisher.objects.get(name=publisher_name)
        if publisher:
            return render(request, 'publisher.html', {'publisher': publisher})
        else:
            return redirect("/")
    except Publisher.DoesNotExist: 
        return redirect("/")




    #select* from post where slug = %slug
    return render(request, 'post.html', locals())



'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append(f'No. {count} - {post} <br>')
        return HttpResponse(post_lists)
'''
