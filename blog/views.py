from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, PostImage


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'post_detail.html', {
        'post':post,
        'photos':photos
    })

# def Register(request):
#
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 != password2:
#             messages.error(request, "Passwords do not match.")
#             return redirect('register.html')
#
#         user = User.objects.create_user(username, email, password1)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
#         return render(request, 'login.html')
#
#     return render(request, "register.html")
#
#
# def Login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid Credentials")
#         return render(request, 'profile.html')
#     return render(request, "login.html")
#
# def Profile(request):
#     return render(request, "profile.html")