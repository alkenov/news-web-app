from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Articles, Comments
from django.views.decorators.cache import cache_page





CACHE_TTL = 60 * 20




@cache_page(CACHE_TTL)
def index(request):
    posts = Articles.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(posts, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'posts': paged_listings}
    return render(request, 'posts.html', context)



def article(request, pk):
    post = get_object_or_404(Articles, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = post
            form.save()
            return redirect(article, pk)
    else:
        form = CommentForm()
    return render(request, 'post.html', {"post": post,
                                         "comments": comment,
                                         "form": form})



def search(request):
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(title__icontains=query)

    context = {
            'listings': queryset_list
        }

    return render(request, 'search.html', context)

