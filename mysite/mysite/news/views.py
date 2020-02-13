from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404

from .models import Articles


def index(request):
    posts = Articles.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(posts, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'posts': paged_listings}
    return render(request, 'posts.html', context)

def article(request, pk):
    post = get_object_or_404(Articles, id=pk)
    return render(request, 'post.html', {"post": post})


def search(request):
    return render(request, 'posts.html')


