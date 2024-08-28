from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse

from .models  import Post
# View recieves a web request and returns a web response
def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.published.all()
    
    # Each view renders a template, passing variables to it, and will return an HTTP response with the rendered output
    return render(
        request,
        template_name='blog/post/list.html',
        context={'posts': posts}, # Any variable set by the template context processors is accessible by the given template
    )

def post_detail(request:HttpRequest, id:int) -> HttpResponse:
    # retriever the object that matches the given parameters or an HTTP404 exception
    post = get_object_or_404(Post, id=id, status=Post.Status.Published)
    
    return render(
        request,
        template_name='blog/post/detail.html',
        context={'post': post},
    )