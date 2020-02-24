from django.shortcuts import render
from news.models import Articles


def index(request):
    if request.method == 'GET':
        posts = Articles.objects.order_by('-list_date')[:3]
        context = {'posts': posts}
        return render(request, context)
