from django.shortcuts import render
from library.models import Post
# Create your views here.
def search_books(request):
    if request.method == 'GET':
        search_query = request.GET.get('keyword', '')
        books = Post.objects.filter(title__icontains=search_query)
        return render(request, 'book.html', {'books': books})
    else:
        return render(request, 'book.html', {'books': []})
    

    