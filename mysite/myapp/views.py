from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "myapp/index.html")
def post(request):
    post = [
        {

        "post1" : "good morning kenya",
        "post2" : "hi hello morning kenya"
            }

    ]
    #context = {post:'post'}
    return render(request, "myapp/post.html")
def posts(request):
    return render(request, "myapp/posts.html")
def profile(request):
    return render(request, "myapp/profile.html")
