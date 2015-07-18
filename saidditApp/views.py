from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
from saidditApp.models import *


def homepage(request):
    c = {}
    c.update({'request': request, 'posts': Post.objects.all()})

    if request.user.is_authenticated():
        c.update({'loggedinuser': request.user.username})
    return render_to_response("saidditApp/index.html", c, context_instance=RequestContext(request))


def viewsubsaidditpage(request, subsaidditname):
    c = {}
    if request.user.is_authenticated():
        c.update({'loggedinuser': request.user})
    try:
        subsaiddit = Subsaiddit.objects.get(name=subsaidditname)
    except Subsaiddit.DoesNotExist:
        return render_to_response("saidditApp/404.html")

    try:
        posts = Post.objects.filter(subsaiddit=subsaiddit)
    except Post.DoesNotExist:
        c.update({'subsaiddit': subsaiddit})
        return render_to_response("saidditApp/viewsubsaiddit.html", c,  context_instance=RequestContext(request))

    c.update({'posts': posts, 'subsaiddit': subsaiddit})
    return render_to_response("saidditApp/viewsubsaiddit.html", c,  context_instance=RequestContext(request))


def registerpage(request):
    c = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        newuser = User.objects.create_user(username, '', password)
        newuser.save()

        return redirect("/login/")
    else:
        return render_to_response("saidditApp/register.html", c, context_instance=RequestContext(request))


def loginpage(request):
    c = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                # Return a 'disabled account' error message
                pass
        else:
            #Not authenticated
            c.update({'message': "Authentication failed"})
            return redirect("/")
            #return render_to_response("saidditApp/index.html", c, context_instance=RequestContext(request))
    else:
        #No one tried login in
        return render_to_response("saidditApp/index.html", c, context_instance=RequestContext(request))


def logoutfunc(request):
    if request.user.is_authenticated():
        logout(request)

    return redirect("/")


def viewpostpage(request, subsaidditname, postid):
    c = {}
    if request.user.is_authenticated():
        c.update({'loggedinuser': request.user})
    try:
        post = Post.objects.get(id=postid)

    except Post.DoesNotExist:
        return render_to_response("saidditApp/404.html")

    try:
        comments = Comment.objects.filter(post=post)
    except Comment.DoesNotExist:
        c.update({'post': post})
        return render_to_response("saidditApp/viewpost.html", c, context_instance=RequestContext(request))

    c.update({'post': post, 'comments': comments})
    return render_to_response("saidditApp/viewpost.html", c, context_instance=RequestContext(request))


def addpostpage(request, subsaidditname):
    c = {}
    if request.user.is_authenticated():
        user = request.user
        c.update({'subsaidditname': subsaidditname})
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            subsaiddit = Subsaiddit.objects.get(name=subsaidditname)
            post = Post(title=title, content=content, score=0, user=user, subsaiddit=subsaiddit)
            post.save()
            return redirect("/r/%s/%d/" % (subsaidditname,post.id))
        else:
            return render_to_response("saidditApp/addpost.html", c, context_instance=RequestContext(request))
    else:
        return redirect("/r/%s" % subsaidditname)


def addcommentfunc(request, postid):
    c = {}
    post = Post.objects.get(id=postid)
    if request.user.is_authenticated():
        user = request.user
        c.update({})
        if request.method == 'POST':
            content = request.POST['content']
            comment = Comment(content=content, score=0, user=user, post=post)
            comment.save()
    subsaidditname = post.subsaiddit.name
    return redirect("/r/%s/%d/" % (subsaidditname, post.id))

def postvotefunc(request, direction, postid, path):
    if request.user.is_authenticated():
        user = request.user
        post = Post.objects.get(id=postid)
        if direction == 'up':
            value = 1
        elif direction == 'down':
            value = -1

        try:
            vote = PostVote.objects.get(user=user, post=post)
        except PostVote.DoesNotExist:
            vote = PostVote(user=user, post=post, direction=value)
            vote.save()

            post.score += value
            post.save()

    if path == "home":
        return redirect("/")
    else:
        subsaidditname = post.subsaiddit.name
        return redirect("/r/%s/" % subsaidditname)



def commentvotefunc(request, direction, commentid):
    if request.user.is_authenticated():
        user = request.user
        comment = Comment.objects.get(id=commentid)
        if direction == 'up':
            value = 1
        elif direction == 'down':
            value = -1

        try:
            vote = CommentVote.objects.get(user=user, comment=comment)
        except CommentVote.DoesNotExist:
            vote = CommentVote(user=user, comment=comment, direction=value)
            vote.save()

            comment.score += value
            comment.save()

        post = comment.post
        subsaidditname = post.subsaiddit.name
        return redirect("/r/%s/%d" % (subsaidditname, post.id))
