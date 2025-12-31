from django.urls import path
from . import views
from .views import CommentListView, CommentDetailView

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment_List'),
    path('/comments/<int:id>/', CommentDetailView.as_view(), name='comment_Detail')
]