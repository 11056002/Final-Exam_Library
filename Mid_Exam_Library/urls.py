from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView, LogoutView
from mysite import views as mv

urlpatterns = [
    # Library Management URLs

    # Mid Exam Library URLs
    path('', mv.homepage, name="homepage"),
    path('default/', mv.showbook, name='default'),
    path('book/', mv.showbook, name='show_book'),
    path('publisher/', mv.showpublisher, name='show_publisher'),
    path('author/', mv.showauthor, name='show_author'),
    path('book/<str:book_name>/', mv.showbook, name='show_book_detail'),
    path('publisher/<str:publisher_name>/', mv.showpublisher, name='show_publisher_detail'),
    path('author/<str:author_name>/', mv.showauthor, name='show_author_detail'),
    path('search_books/', mv.search_books, name='search_books'),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('loginpage', views.home_view),
    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),
    path('studentsignup', views.studentsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html')),
    path('returnbook/<int:id>/', views.returnbook, name='returnbook'),
    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),
    path('addbook', views.addbook_view),
    path('deletebook',views.deletebook_view),
    path('viewbook', views.viewbook_view),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent, name='viewissuedbookbystudent'),
    path('aboutus', views.aboutus_view),

]
