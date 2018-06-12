from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from articles.models import Articles

# Create your views here.db.sqlite3
from blogs.forms import PostForm
from blogs.models import Blogs

@login_required(login_url="/login/")

def blogs(request):
    query = request.GET.get("q")
    if query:
        return render_to_response('blogs.html', {'user': request.user,'blogs': Blogs.objects.filter(
            Q(title__icontains=query) |
            Q(user__username__icontains=query)
        ).distinct()})
    else:
        return render_to_response('blogs.html', {'user': request.user,'blogs': Blogs.objects.all()})

@login_required(login_url="/login/")

def blog(request, blog_id):
    articles_in_blog = Articles.objects.filter(blog_id=blog_id)
    blog=get_object_or_404(Blogs, id=blog_id)

    query = request.GET.get("q")
    if query:
        return render_to_response('blog.html', {'user': request.user,'blog': articles_in_blog.filter(
            Q(title__icontains=query) |
            Q(user__username__icontains=query) |
            Q(content__icontains=query)
        ).distinct(),'user': blog.user, 'title': blog.title})
    else:
        return render_to_response('blog.html', {'user': request.user,'blog': Articles.objects.filter(blog_id=blog_id), 'user': blog.user, 'title': blog.title})


@login_required(login_url="/login/")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published = timezone.now()
            post.save()
            return redirect('blogs:blog', blog_id=post.id)
    else:
        form = PostForm()
    return render(request, 'add_blog.html', {'user': request.user,'form': form})
