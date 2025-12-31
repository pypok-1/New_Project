from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from .models import Comment, Post


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    paginate_by = 5

    def get_queryset(self):
        self.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return Comment.objects.filter(post=self.post).select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post
        return context

class CommentDetailView(DetailView):

