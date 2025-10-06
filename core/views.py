from .models import Leadership
# Leadership Board View
from django.views.generic import ListView

class LeadershipListView(ListView):
    model = Leadership
    template_name = 'core/leadership.html'
    context_object_name = 'leadership_list'
# core/views.py
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.db.models import Q
from .models import Division, AboutPage, ContactInquiry, Event, DivisionImage
from django.views.generic import DetailView
class DivisionDetailView(DetailView):
    model = Division
    template_name = 'core/division_detail.html'
    context_object_name = 'division'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_images'] = DivisionImage.objects.filter(division=self.object)[:3]
        return context
from .forms import ContactForm
from django.shortcuts import render, redirect

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['divisions'] = Division.objects.all()[:3]
        context['events_list'] = Event.objects.order_by('-date')[:3]
        from .models import Leadership, Award, AboutPage
        context['leadership_list'] = Leadership.objects.all()[:3]
        context['awards_list'] = Award.objects.order_by('-year')[:3]
        # Add latest news
        from news.models import NewsArticle
        context['news_list'] = NewsArticle.objects.order_by('-publish_date')[:4]
        context['about_page'] = AboutPage.objects.first()
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_page'] = AboutPage.objects.first()
        return context

class DivisionListView(ListView):
    model = Division
    template_name = 'core/divisions.html'
    context_object_name = 'divisions'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(sector__icontains=query)
            )
        return queryset

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('core:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})