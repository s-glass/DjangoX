from django.urls import path
from .views import SongListView, SongDetailView, SongCreateView, SongUpdateView, SongDeleteView

urlpatterns = [
    path('', SongListView.as_view(), name='list_view'),
    path('<int:pk>', SongDetailView.as_view(), name='detail_view'),
    path('new', SongCreateView.as_view(), name='create_view'),
    path('<int:pk>/edit', SongUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', SongDeleteView.as_view(), name='delete_view'),
]