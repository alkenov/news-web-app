from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Articles


def index(request):
    listings = Articles.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}
    return render(request, 'posts.html', context)


def listing(request, listing_id):
    return render(request, 'posts.html')


def search(request):
    return render(request, 'posts.html')