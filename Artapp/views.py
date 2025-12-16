from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

def home(request):
    return render(request, 'index.html')

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article_list.html', {'articles': articles})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list') 
    else:
        form = ArticleForm()
    
    return render(request, 'article_form.html', {'form': form, 'title': 'Создать статью'})

def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')  
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'article_form.html', {'form': form, 'title': 'Редактировать статью', 'article': article})