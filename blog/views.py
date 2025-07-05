from django.urls import reverse_lazy, reverse

from blog.models import Post
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView


class BlogListView(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"

    def get_queryset(self):
        return super().get_queryset().filter(publication_attribute=True)

class BlogCreateView(CreateView):
    model = Post
    fields = ["header", "content", "preview", "views_counter"]
    template_name = "blog_form.html"
    success_url = reverse_lazy("blog:blog")

class BlogUpdateView(UpdateView):
    model = Post
    fields = ["header", "content", "preview", "views_counter"]
    template_name = "blog_form.html"
    success_url = reverse_lazy("blog:blog")

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get("pk")])

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog')