from django.db.models import Q, Count
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .models import Index, Base, Portfolio, Network, Comment, Category, Tag, About, Contact, Contact_Message
from django.core.paginator import Paginator


def for_all(request):
    obj = Base.objects.first
    return {'base': obj}


def IndexView(request):
    obj = Index.objects.first
    post = Portfolio.objects.all()
    p = Paginator(post, 12)
    page = request.GET.get('page')
    post = p.get_page(page)
    categor = Category.objects.all()
    tag = Tag.objects.all()
    popular = Portfolio.objects.order_by('-view')[:5]
    commented_portfolios = Comment.objects.order_by('-created')[:5]
    context = {
        'category': categor,
        "home": obj,
        'product': post,
        'tag': tag,
        'popular': popular,
        'comment': commented_portfolios
    }
    return render(request, 'index.html', context)


def About_Me(request):
    obj = About.objects.first
    home = Index.objects.first
    context = {
        'home': home,
        'about': obj
    }
    return render(request, 'about-me.html', context)


def Search(request):
    home = Index.objects.first
    text = request.GET.get('search')
    obj = Portfolio.objects.filter(
        Q(name__contains=text) |
        Q(category__name__contains=text) |
        Q(coloborator__name__contains=text) |
        Q(tag__name__contains=text)
    ).distinct()
    categor = Category.objects.all()
    tag = Tag.objects.all()
    popular = Portfolio.objects.order_by('-view')[:5]
    commented_portfolios = Comment.objects.order_by('-created')[:5]
    context = {
        'category': categor,
        'product': obj,
        'home': home,
        'tag': tag,
        'popular': popular,
        'comment': commented_portfolios
    }
    return render(request, 'index.html', context)


def Detail_Post(request, pk):
    obj = get_object_or_404(Portfolio, pk=pk)
    obj.increment_view_count(request)
    tag = Tag.objects.all()
    popular = Portfolio.objects.order_by('-view')[:5]
    commented_portfolios = Comment.objects.order_by('-created')[:5]
    categor = Category.objects.all()
    context = {
        "detail": obj,
        'category': categor,
        'tag': tag,
        'popular': popular,
        'comment': commented_portfolios
    }
    return render(request, 'blog-post-no-featured-image.html', context)


def Add_Comment(request, pk, comment_pk=None):
    post = Portfolio.objects.get(pk=pk)
    name = request.GET.get('name')
    email = request.GET.get('email')
    comment = request.GET.get('comment')
    com = Comment.objects.create(
        post=post,
        user=name,
        body=comment,
        email=email,
        reply=comment_pk
    )
    com.save()
    return redirect('detail_post', pk=pk)


def Detail_Tag(request, pk):
    categor = Category.objects.all()
    home = Index.objects.first
    obj = Portfolio.objects.filter(tag__pk=pk)
    tag = Tag.objects.all()
    popular = Portfolio.objects.order_by('-view')[:5]
    commented_portfolios = Comment.objects.order_by('-created')[:5]
    context = {
        'category': categor,
        'product': obj,
        'home': home,
        'tag': tag,
        'popular': popular,
        'comment': commented_portfolios
    }
    return render(request, 'index.html', context)


def Detail_Author(request, pk):
    categor = Category.objects.all()
    home = Index.objects.first
    obj = Portfolio.objects.filter(coloborator__pk=pk)
    tag = Tag.objects.all()
    popular = Portfolio.objects.order_by('-view')[:5]
    commented_portfolios = Comment.objects.order_by('-created')[:5]
    context = {
        'category': categor,
        'product': obj,
        'home': home,
        'tag': tag,
        'popular': popular,
        'comment': commented_portfolios
    }
    return render(request, 'index.html', context)


def CategoryView(request, pk):
    categor = Category.objects.all()
    home = Index.objects.first
    obj = Portfolio.objects.filter(category__pk=pk)
    tag = Tag.objects.all()
    popular = Portfolio.objects.order_by('-view')[:5]
    commented_portfolios = Comment.objects.order_by('-created')[:5]
    context = {
        'category': categor,
        'product': obj,
        'home': home,
        'tag': tag,
        'popular': popular,
        'comment': commented_portfolios
    }
    return render(request, 'index.html', context)


class ContactView(View):
    def get(self, request):
        obj = Contact.objects.first
        context = {
            'contact': obj
        }
        return render(request, 'contact.html', context)

    def post(self, request):
        data = request.POST
        print(data)
        Contact_Message.objects.create(name=data['name'],
                                   email=data['email'],
                                   option=data['option'],
                                   message=data['message'])
        return redirect('contact')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request, *args, **kwargs):
    return render(request, '500.html', status=500)
