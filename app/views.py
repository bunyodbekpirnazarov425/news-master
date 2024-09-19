from django.contrib.auth import login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from .models import News, Category
from .forms import RegisterForm, LoginForm

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

def register(request: WSGIRequest):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            # print(f"{user.username} user yaratildi")
            return redirect("login")
        else:
            print(form.error_messages, "**********")
    else:
        form = RegisterForm()
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def user_login(request: WSGIRequest):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def user_logout(request):
    logout(request)
    return redirect("login")

def about(request, pk):
    news = News.objects.get(pk=pk)
    context = {
        "news": news,
    }
    return render(request, "about.html", context)