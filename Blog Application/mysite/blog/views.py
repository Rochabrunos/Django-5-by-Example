from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from .forms import EmailPostForm
from .models  import Post


class PostListView(ListView): #ListView allows to list any type of object
    """Alternative post list view"""
    # Defines a custom QuerySet, it is possible to specified model = Post
    queryset = Post.published.all()
    # We use the context variable posts for the query results (default variable is object_list)
    context_object_name = 'posts'
    # We define pagination os results returnig three objects per page
    paginate_by = 3
    # Defines custom template to render the page (default template is blog/post_list.html)
    template_name = 'blog/post/list.html'

def post_detail(request:HttpRequest, year:int, month:int, day:int, post:str) -> HttpResponse:
    # retriever the object that matches the given parameters or an HTTP404 exception
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    return render(
        request,
        template_name='blog/post/detail.html',
        context={'post': post},
    )

# Why not a class-based view form instead function-based one
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()

    return render(
        request,
        template_name='blog/post/share.html',
        context={
            'post': post,
            'form': form,
        }
    )