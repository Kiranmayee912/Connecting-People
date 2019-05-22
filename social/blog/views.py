from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


from .models import Post,Upload
from django.contrib.auth.models import User
from users.models import Profile

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def timeline(request,pk):
    q1 = Post.objects.filter(author__pk= pk).order_by('date_posted')
    q2 = Upload.objects.filter(author__pk= pk).order_by('date_posted')
    u= User.objects.filter(id=pk).first()
    return render(request, 'blog/timeline.html', {'posts': q1, 'uploads': q2,'user':u})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

def search(request):
    u=request.GET.get('u')
    susers=User.objects.filter(username__icontains=u)
    return render(request,'blog/search.html',{'susers':susers})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})









class UploadListView(ListView):
    model = Upload
    template_name = 'blog/upload_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    ordering = ['-date_posted']


class UploadDetailView(DetailView):
    model = Upload


class UploadCreateView(LoginRequiredMixin, CreateView):
    model = Upload
    fields = ['title','caption','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UploadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Upload
    fields = ['title','caption','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UploadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Upload
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
