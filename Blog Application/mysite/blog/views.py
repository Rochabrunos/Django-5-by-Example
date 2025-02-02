from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.views.decorators.http import require_POST

from taggit.models import Tag

from .forms import EmailPostForm, CommentForm
from .models  import Post

class PostListView(ListView): #ListView allows to list any type of object
    """Alternative post list view"""
    # Defines a custom QuerySet, it is possible to specified model = Post
    # queryset = Post.published.all()
    # We use the context variable posts for the query results (default variable is object_list)
    context_object_name = 'posts'
    # We define pagination os results returnig three objects per page
    paginate_by = 3
    # Defines custom template to render the page (default template is blog/post_list.html)
    template_name = 'blog/post/list.html'

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        if tag_slug is not None:
            return Post.published.filter(tags__slug=tag_slug)
        return Post.published.all()
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        tag_slug = self.kwargs.get("tag_slug")
        if tag_slug is not None:
            context["tag"] = Tag.objects.filter(slug=tag_slug).first()
            return context
        return context

def post_detail(request:HttpRequest, year:int, month:int, day:int, post:str) -> HttpResponse:
    # retriever the object that matches the given parameters or an HTTP404 exception
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    comments = post.comments.filter(active=True)
    form = CommentForm()

    return render(
        request,
        template_name='blog/post/detail.html',
        context={
            'post': post,
            'comments': comments,
            'form': form,},
    )

# Why not a class-based view form instead function-based one
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )
    # Used to display a success message when the form is successufully submitted
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(  # Build a complete URL, i.e. with Http schema and hostname
                post.get_absolute_url(), # Retrives the absolute path of the post
            )
            subject = (
                f'{ cd["name"] } <{ cd["email"] }>'
                f' recommends you read { post.title }'
            )
            message = (
                f'Read { post.title } at { post_url }\n\n'
                f'{ cd["name"] }\'s comments: PUT COMMENTS IN HERE'
            )
            # From_email=None the default value will be the DEFAULT_FROM_MAIL
            if send_mail(subject, message, from_email=None, recipient_list=[cd['to']]) == 1:
                sent = True

    else:
        form = EmailPostForm()

    return render(
        request,
        template_name='blog/post/share.html',
        context={
            'post': post,
            'form': form,
            'sent': sent,
        }
    )

# Django will throw an HTTP 405 error if you try to access the view with any other HTTP method
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED,
    )
    comment = None

    form = CommentForm(data=request.POST)

    if form.is_valid():
        # Commit=false the model instance is created but not saved to the database
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    
    return render(
        request,
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment,
        }
    )
