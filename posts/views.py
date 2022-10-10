from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Status




class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    status = "published"

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) 
      pending_status = Status.objects.get(name=self.status)
      context['post_list'] = Post.objects.filter(status=pending_status).order_by('created_on').reverse()
      return context                      
   

class DraftPostListView(ListView):
    template_name = "posts/list.html" 
    model = Post


    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) 
      pending_status = Status.objects.get(name="draft")
      context['post_list'] = Post.objects.filter(author=self.request.user).filter(status=pending_status).order_by('created_on').reverse()
      return context                      
                                 
                                
                                    
                                        
                                    
               



class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post




class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle",  "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html" 
    model = Post
    fields = ["title", "subtitle", "body"]
    def test_func(self):
        post_obj = self.get_object()
        return post_object.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"  
    model = Post
    success_url = reverse_lazy("list")
    def test_func(self):
        post_obj = self.get_object()
        return post_object.author == self.request.user 