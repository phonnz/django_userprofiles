from django.shortcuts import render
from django.views.generic import  DetailView

from braces.views import LoginRequiredMixin

from .models import *

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = '/'
    context_object_name = 'post'

    def get_comments(self, post):
        return Comment.objects.filter(Post = post)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = self.get_comments(context['object'])

        return context

    def post(self, request, *args, **kwargs):
        comment= Comment()
        comment.comment = request.POST['comment']
        comment.Post = Post.objects.get(pk = kwargs['pk'])
        comment.save()
        comments = self.get_comments(comment.Post)
        return render(request, 'post_detail.html', {'post':comment.Post, 'comments':comments})
