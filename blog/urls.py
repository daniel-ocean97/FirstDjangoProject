from django.urls import path

from blog.apps import BlogConfig

from . import views

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", views.BlogListView.as_view(), name="blog"),
    path("blog/create", views.BlogCreateView.as_view(), name="post_create"),
    path("blog/detail/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail"),
    path("blog/update/<int:pk>/", views.BlogUpdateView.as_view(), name="post_update"),
    path("blog/delete/<int:pk>/", views.BlogDeleteView.as_view(), name="post_delete"),
]
