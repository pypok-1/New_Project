from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from .models import Comment, Post
from django.contrib.auth.models import User


class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    paginate_by = 5
    context_object_name = 'comments'

    def get_queryset(self):
        self.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return Comment.objects.filter(post=self.post).select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post
        return context


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comments/comment_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'comments'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'comments/comment_form.html'

    def form_valid(self, form):
        self.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = self.post
        form.instance.author = self.request.user
        return super().form_valid(form)

