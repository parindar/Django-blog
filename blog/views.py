from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Tag
from .models import Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.order_by('published_date')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
	        comment = form.save(commit=False)
	        comment.post = Post.objects.get(post_id = request.POST.get('post_id'))
	        comment.date = timezone.now()
	        comment.save()
	        form = CommentForm()
	        return render(request, 'blog/post_list.html', {'posts': posts , 'form': form})
    else:
        form = CommentForm()

    return render(request, 'blog/post_list.html', {'posts': posts , 'form': form})

