from django.http import HttpResponse,HttpResponseRedirect
from .models import Articles,Comment, Blogs
from django.shortcuts import get_object_or_404, render_to_response,render
from django.db.models import Q
from django.utils import timezone
from articles.forms import CommentForm
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def post_new(request):
    user_blogs = Blogs.objects.filter(user_id=request.user.id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published = timezone.now()
            password=request.POST['password']
            isProtected=request.POST.get("isProtected")
            if isProtected == "True":
                post.isProtected=True
            if password != "":
                post.password=password
            selectedBlog = request.POST['user_blogs']
            blog = Blogs.objects.get(title=selectedBlog)
            post.blog = blog
            post.save()
            return redirect('article:article', article_id=post.id)
    else:
        form = PostForm()

    return render(request, 'post_edit.html', {'form': form, 'user': request.user, 'user_blogs': user_blogs })


@login_required(login_url="/login/")
def articles(request):
    newest =Articles.objects.order_by('-published')

    query = request.GET.get("q")
    if query:
        return render_to_response('articles.html', {'newest':newest, 'allarticles':Articles.objects.all(),'user': request.user,'articles': Articles.objects.filter(
            Q(title__icontains=query) |
            Q(user__username__icontains=query)
        ).distinct()})
    else:
        return render_to_response('articles.html', {'newest':newest, 'allarticles':Articles.objects.all(),'user': request.user,'articles': Articles.objects.all()})

@login_required(login_url="/login/")
def article(request, article_id, comesFromComment = False):
    article = get_object_or_404(Articles, id=article_id)
    print(comesFromComment)
    if article.isProtected and comesFromComment == False:
        if request.method == "POST":
            form = PostForm(request.POST)
            password = request.POST["password"]
            if password == article.password:
                return render(request, 'article.html', {'user': request.user,'article': article})
            else:
                return render(request, 'auth/password.html', {'error': 'Nieprawidlowe hasło', 'user': request.user,'article': article})
        else:
            form = PostForm()
            return render(request, 'auth/password.html', {'user': request.user,'article': article})
    else:
        return render(request, 'article.html', {'user': request.user,'article': article})


@login_required(login_url="/login/")
def addcomment(request, a_id):
    article_ = get_object_or_404(Articles, id=a_id)
    if request.method == 'POST':
        print("sprawdzenie")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user=request.user
            comment.published = timezone.now()
            comment.article = article_
            comment.save()
            response = article(request,article_id=a_id, comesFromComment= True)
        return response
    else:
        form = CommentForm()
        context = {'form': form,'user': request.user, 'article_id': a_id}

    return render(request, 'addcomment.html', context)

