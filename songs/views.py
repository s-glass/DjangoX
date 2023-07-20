from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Song
from django.urls import reverse_lazy


class SongListView(ListView):
    template_name = 'song-list.html'
    model = Song
    context_object_name = 'songs'


class SongDetailView(DetailView):
    template_name = 'song-detail.html'
    model = Song


class SongCreateView(CreateView):
    template_name = 'song-create.html'
    model = Song
    fields = ['title', 'owner', 'description']


class SongUpdateView(UpdateView):
    template_name = 'song-update.html'
    model = Song
    fields = ['title', 'owner', 'description']


class SongDeleteView(DeleteView):
    template_name = 'song-delete.html'
    model = Song
    success_url = reverse_lazy('list_view')