from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    all_news = News.objects.all().order_by('-date')  # show latest first

    # Count news by category
    category_counts = {
        'Travels': News.objects.filter(category='travels').count(),
        'Organization': News.objects.filter(category='organization').count(),
        'Tips & Tricks': News.objects.filter(category='tips').count(),
        'Uncategorized': News.objects.filter(category='uncategorized').count(),
        'Latest News': News.objects.filter(category='latest').count(),
    }

    context = {
        'all_news': all_news,
        'category_counts': category_counts
    }
    return render(request, 'news.html', context)

def news_by_category(request, category):
    all_news = News.objects.filter(category__iexact=category).order_by('-date')
    context = {
        'all_news': all_news,
        'selected_category': category
    }
    return render(request, 'news.html', context)