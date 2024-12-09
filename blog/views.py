from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
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


# class PostCreateView(FormView):
#     # The template used to render the form.
#     template_name = 'blog/post_create.html'

#     # The form class that defines the structure and validation logic for the form.
#     form_class = PostForm

#     # URL to redirect to after successfully creating a new post.
#     success_url = reverse_lazy('blog:post_list')

#     def form_valid(self, form):
#         """
#         Called when the form is submitted and validated successfully.
#         - Saves the form instance (e.g., the Post object) to the database.
#         - Calls the parent class's form_valid method to handle redirection.
#         """
#         form.save()
#         return super().form_valid(form)

class PostCreateView(CreateView):
    """
    Handles the creation of a new blog post.
    Renders a form for the user to fill out and saves the post upon validation.
    """
    model = models.Post  # Specifies the model associated with this view.
    form_class = PostForm  # Custom form class for creating a post (uncomment to use).
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']  # Alternative to `form_class`.

    template_name = 'blog/post_create.html'  # Template for rendering the form.
    success_url = reverse_lazy('blog:post_list')  # Redirects to the post list upon successful creation.

    def form_valid(self, form):
        """
        Automatically assigns the current user as the author of the post.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    """
    Handles editing an existing blog post.
    Renders a form pre-filled with the post's data for updating.
    """
    model = models.Post  # Specifies the model associated with this view.
    form_class = PostForm  # Custom form class for editing a post (uncomment to use).
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']  # Alternative to `form_class`.

    template_name = 'blog/post_create.html'  # Template for rendering the form.
    success_url = reverse_lazy('blog:post_list')  # Redirects to the post list upon successful update.
