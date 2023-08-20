from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category, Comment
from django.db.models import Q
from dashboards.forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the posts that belongs to this category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # use try/except when we want to do some custom action if the category does not exist
    # try:
        # category = get_object_or_404 (Category, pk=category_id)
    # except:
        # redirect user to homepage
        # return redirect('home')
    # use get_object_or_404 when you want to show 404 error page if category does not exit
    category = get_object_or_404 (Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    form = CommentForm()
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
        'form': form
    }
    return render(request, 'blogs.html', context) 

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)

