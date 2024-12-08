from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView
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
    # This view handles the creation of a new blog post by rendering a form and saving the post once the form is valid.
    
    # The model associated with the view (in this case, it's the Post model).
    # This tells Django that the form will create instances of the `Post` model.
    model = models.Post
    
    # The form class is commented out here, but if you want to use a custom form instead of 
    # the default model form, you can define and use a `PostForm` class.
    # Uncomment the following line to use a custom form class.
    form_class = PostForm

    # The fields of the model that will be displayed in the form. 
    # This list determines which fields are included in the form for the user to fill out.
    # The list includes author, title, content, status, category, and published_date.
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    
    # The template that will be used to render the form. 
    # It specifies the HTML file where the form will be displayed to the user.
    template_name = 'blog/post_create.html'

    # The URL to which the user will be redirected after successfully creating a new post.
    # In this case, after a successful form submission, the user will be redirected to the blog post list page.
    success_url = reverse_lazy('blog:post_list')
    # `reverse_lazy` is used here because it resolves the URL at runtime, 
    # after the URLconf has been loaded, which is necessary for class-based views.

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)