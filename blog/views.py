from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from blog import models
from blog.form import PostForm


class PostListView(ListView):
    # The model that this view is working with. Automatically fetches all objects of this model.
    model = models.Post

    # Alternative method 1: Explicitly specify the queryset to be used.
    # queryset = models.Post.objects.all()

    # Alternative method 2: Customize the queryset by overriding get_queryset.
    # def get_queryset(self):
    #     posts = models.Post.objects.all()
    #     return posts

    # By default, Django passes the object list to the template as 'object_list'.
    # To use a custom context name (e.g., 'posts'), specify it here.
    context_object_name = 'posts'

    # Enables pagination. Limits the number of posts displayed per page.
    paginate_by = 2

    # Orders the posts by descending ID. If this is used, avoid overriding get_queryset.
    ordering = '-id'


class PostDetailView(DetailView):
    # The model whose details are displayed. The selected instance is passed to the template as 'object' by default.
    model = models.Post

    # Tip: If you want a custom context name instead of 'object', override `context_object_name`.


class PostCreateView(FormView):
    # The template used to render the form.
    template_name = 'blog/post_create.html'

    # The form class that defines the structure and validation logic for the form.
    form_class = PostForm

    # URL to redirect to after successfully creating a new post.
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        """
        Called when the form is submitted and validated successfully.
        - Saves the form instance (e.g., the Post object) to the database.
        - Calls the parent class's form_valid method to handle redirection.
        """
        form.save()
        return super().form_valid(form)
