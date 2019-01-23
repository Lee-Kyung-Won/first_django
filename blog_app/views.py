from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog_app/post_list.html', {
        'post_list': qs,
        'q': q,
    })