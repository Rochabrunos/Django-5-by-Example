from django import forms

from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

class CommentForm(forms.ModelForm):
    class Meta:
        # Django will introspect the model and build the corresponding form dinamically
        model = Comment
        # Defines which fields are included in the form (the opposite is exclude)
        fields = ['name', 'email', 'body']