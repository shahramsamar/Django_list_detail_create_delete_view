from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog import models




class PostListView(ListView):
    # three way use  this  methods
    
    model = models.Post
    
    # queryset = models.Post.objects.all()
    
    # def get_queryset(self):
    #      posts =models.Post.objects.all()
    #      return posts
     
    # if not write this  method ,you must use name (object_list) 
    context_object_name = 'posts'
    
    # for example if you have a posts object
    paginate_by = 1
    
    # when i use ordering, i dont use get_queryset
    ordering = '-id'
    

class PostDetailView(DetailView):
    
    # you must use in (object)
    model = models.Post
      
 