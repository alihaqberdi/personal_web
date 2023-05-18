from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='homepage'),
    path('ali/', views.About_Me, name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post/<int:pk>/', views.Detail_Post, name="detail_post"),
    path('comment/<int:pk>/', views.Add_Comment, name='addcomment'),
    path('search/', views.Search, name='search'),
    path('tag/<int:pk>/', views.Detail_Tag, name='tagname'),
    path('popular/', views.Detail_Tag, name='popular'),
    path('author/<int:pk>/', views.Detail_Author, name='author'),
    path('category/<int:pk>/', views.CategoryView, name='categories'),
]
