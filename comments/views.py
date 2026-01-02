from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    context_object_name = 'comment'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'comments/comment_form.html'

    def form_valid(self, form):
        self.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = self.post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comment_list', kwargs={'post_id': self.post.id})


class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    fields = ['text']
    template_name = 'comments/comment_form.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('comment_detail', kwargs={'pk': self.object.id})


class CommentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin ):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('comment_list', kwargs={'post_id': self.object.post.id})
