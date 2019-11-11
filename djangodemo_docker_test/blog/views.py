from django.shortcuts import render
from .models import Post
from .form import PostForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

'''
!!!!! 2019.11.07 You can't have a default that involves a query on the database. 
That will airways be executed on first import, 
do the migration that creates the table will never have a chance to run. 
Remove the default.
'''

# me = get_user_model().objects.get(username='lionel771128')
# Create your views here.
def post_list(request):
    posts = Post.objects.all()\
        .order_by('-created_date')
    post_form = PostForm()

    # return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'blog/post_list.html', locals())

def post_form(request):
    form = PostForm()
    return render(request, 'blog/post_list.html', {'post_form': form})

def add_record(request):
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        text = data['text']
        Post.objects.create(title=title, text=text, author=me)
    return redirect('/blog')

def post_record(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_record.html', locals())
