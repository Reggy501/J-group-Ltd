# core/urls.py
from django.urls import path
from .views import HomeView, AboutView, DivisionListView, contact, LeadershipListView, DivisionDetailView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('divisions/', DivisionListView.as_view(), name='divisions'),
    path('divisions/<slug:slug>/', DivisionDetailView.as_view(), name='division_detail'),
    path('contact/', contact, name='contact'),
    path('leadership/', LeadershipListView.as_view(), name='leadership'),
]