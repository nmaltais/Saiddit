from django.shortcuts import render_to_response

# Create your views here.
from saidditApp.models import *


def homepage(request):
    return render_to_response("saidditApp/index.html", {
        'subsaiddits': Subsaiddit.objects.all()
    })


def viewsubsaidditpage(request, subsaidditname):

    try:
        subsaiddit = Subsaiddit.objects.get(name=subsaidditname)
    except Subsaiddit.DoesNotExist:
        return render_to_response("saidditApp/404.html")

    try:
        posts = Post.objects.filter(subsaiddit=subsaiddit)
    except Post.DoesNotExist:

        return render_to_response(("saidditApp/viewsubsaiddit.html"), {
            'subsaiddit' : subsaiddit
        })

    return render_to_response("saidditApp/viewsubsaiddit.html", {
        'posts': posts,
        'subsaiddit': subsaiddit
    })


def loginpage(request):
    return render_to_response("saidditApp/login.html", {
        'users': User.objects.all()
    })


def viewpostpage(request, postid):
    try:
        post = Post.objects.get(id=postid)

    except Post.DoesNotExist:
        return render_to_response("saidditApp/404.html")

    try:
        comments = Comment.objects.filter(post=post)
    except Comment.DoesNotExist:
        return render_to_response("saidditApp/viewpost.html", {
            'post': post
        })

    return render_to_response("saidditApp/viewpost.html", {
            'post': post,
            'comments': comments
        })

