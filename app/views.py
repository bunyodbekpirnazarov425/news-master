from django.shortcuts import render
from .models import News, Category

# def home(request):
#     newses = News.objects.all()
#     order_newses = newses.order_by('-update')
#     news_popular = newses.filter(is_active=True, is_popular=True).first()
#     news_top_story = newses.order_by("-created").first()
#     trending_news = newses.order_by("-created")[:8]
#     categories = Category.objects.all()
#     newses_all = order_newses[:6]
#
#     context = {
#         'newses_all': newses_all,
#         'news_popular': news_popular,
#         'news_top_story': news_top_story,
#         'trending_news': trending_news,
#         'categories': categories,
#     }
#
#     return render(request, 'index.html', context)

def home(request):
    newses = News.objects.all()
    order_newses = newses.order_by('-update')
    news_top = newses.filter(is_active=True, is_popular=True)
    news_popular = newses.filter(is_active=True, is_popular=True).first()
    news_top_story = newses.order_by("-created").first()
    trending_news = newses.order_by("-created")[:8]
    categories = Category.objects.all()
    newses_all = order_newses[:6]

    context = {
        'newses_all': newses_all,
        'news_popular': news_popular,
        'news_top_story': news_top_story,
        'trending_news': trending_news,
        'categories': categories,
        'news_top': news_top,
    }

    return render(request, 'index.html', context)
