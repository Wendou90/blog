from django.urls import path
from .views import (
    PostListView,
    DraftPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('drafts/', DraftPostListView.as_view(), name='draft_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]