# news/urls.py
from django.urls import path
from .views import NewsListView, NewsDetailView

app_name = 'news'
urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
]