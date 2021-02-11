from django.shortcuts import render
from blog.forms import BlogForm
from django.http import HttpResponseRedirect
from blog.models import Blog
# Create your views here.
def index(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        form.save()
        return HttpResponseRedirect('blog-view/')
    else:
        form = BlogForm
        context = {
            'form': form,
        }
        return render(request, "blog/index.html", context)

def blog_view(request):
    context = {
        'blogs': Blog.objects.all(),
    }
    return render(request,"blog/blog_view.html", context)