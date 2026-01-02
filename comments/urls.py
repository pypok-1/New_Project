from django.urls import path
from . import views
from .views import CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment_List'),
    path('comments/<int:id>/', CommentDetailView.as_view(), name='comment_Detail'),
    path('posts/<int:post_id>/comments/create/', CommentCreateView.as_view(), name='comment_Create'),
    path('comments/<int:id>/update/', CommentUpdateView.as_view(), name='comment_Update'),
    path('comments/<int:id>/delete/', CommentDeleteView.as_view(), name='comment_Delete')
]
