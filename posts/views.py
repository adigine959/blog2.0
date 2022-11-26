from django.shortcuts import render
import datetime
from .models import *


def hello(request):
    return render(request, 'hello.html')
def goodby (request):
    return render(request, 'goodby.html')
def now_date (request):
    a = datetime.datetime.now()
    return render(request, 'now_date.html',{'a':a})



def hashtags(request):
    if request.method == "GET":
        data = {'hashtags': Hashtag.objects.all()}
        return render(request, 'hashtags.html', context=data)


#def posts(request):
 #   data = {'posts': Post.objects.all()}
   # return render(request, 'posts.html', context=data)
def posts(request):
    if request.method == 'GET':
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            hashtag = Hashtag.objects.get(id=hashtag_id)
            posts = Post.objects.filter(hashtag=hashtag)
        else:
            posts = Post.objects.all()
        data = {
            'posts': Post.objects.all(),
            'post': posts
        }
        return render(request, 'posts.html', context=data)


def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        data = {
            'post': post,
            'comments': Comment.objects.filter(post=post),
            'form': CommentCreateForm
        }
        return render(request, 'post_detail.html', context=data)
    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs['id'])
            comments = Comment.objects.filter(post=post)

            data = {
                'post': post,
                'comments': comments,
                'form': form
            }

            return render(request, 'posts/post_detail.html', context=data)

    def post_create_view(request):
        if request.method == 'GET':
            data = {
                'form': PostCreateForm
            }
            return render(request, 'posts/creat.html', context=data)
        if request.method == 'POST':
            form = PostCreateForm(data=request.POST)

            if form.is_valid():
                Post.objects.create(
                    title=form.cleaned_data.get('title'),
                    description=form.cleaned_data.get('description')
                )
                return redirect('/posts/')
            else:
                data = {
                    'form': form
                }
                return render(request, 'posts/creat.html', context=data)

