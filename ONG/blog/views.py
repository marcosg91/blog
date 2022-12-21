from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *




# Create your views here.
def HomeView(request):
    template_name = "home.html"
    #articulos = Noticias.objects.filter(status='publish')
    #context = {'articulos': articulos}
    return render(request, template_name )#, context=context)


def Noticias(request):
    template_name = "Noticias.html"
    articulos = Noticias.objects.filter(status='publish')
    context = {'articulos': articulos}
    return render (request, template_name, context)

def CategoryView(request, cats):
    template_name = 'category.html'
    category_post = Noticias.objects.filter(category__slug=cats, status='publish')
    context = {'category': cats, 'category_post': category_post}
    return render(request, template_name, context)


def postdetail(request, post):
    template_name = 'single.html'
    post = get_object_or_404(Noticias, slug=post, status='publish') 
    comment = post.comment_post.filter(active=True)
    
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            #new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            comment_form.instance.post = post
            comment_form.instance.author = request.user
            # Save the comment to the database
            comment_form.save()
    else:
        comment_form = CommentForm()

    context = {'post': post, 'comments': comments,'comment_form': comment_form}
    return render(request, template_name, context)




def  registerView(request):
    template_name =  "registration/register.html"
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()

    context={"form": form}
    return render (request, template_name ,context)



def Quienes_somos(request):
    return render (request, "social/Quienes_somos.html")





