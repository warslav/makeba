from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleCommentView,
)

urlpatterns = [
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/new/', ArticleCreateView.as_view(), name='article_new'),
    path('articles/<int:article_id>/comment/', ArticleCommentView.as_view(), name='article_comment'),
    path('', ArticleListView.as_view(), name='article_list'),
]
