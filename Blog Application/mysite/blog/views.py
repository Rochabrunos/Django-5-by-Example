from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage

from .models  import Post
# View recieves a web request and returns a web response
def post_list(request: HttpRequest) -> HttpResponse:
    post_list = Post.published.all()
    
    # Pagination with 3 posts per page
    paginator = Paginator(object_list=post_list, per_page=3)
    page_number = request.GET.get(key='page', default=1)
    try:
        # page() method returns a Page object
        posts = paginator.page(number=page_number)
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)

    # Each view renders a template, passing variables to it, and will return an HTTP response with the rendered output
    return render(
        request,
        template_name='blog/post/list.html',
        context={'posts': posts}, # Any variable set by the template context processors is accessible by the given template
    )

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