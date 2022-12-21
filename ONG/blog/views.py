from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib import messages
from .models import *
from .forms import UserRegistrationForm, CommentForm


def HomeView(request):
    template = 'home.html'
    #posts = Publicación.objects.filter(status='publish')
    post3 = Publicación.objects.filter(status='publish')[:6]
    #menu_intems = NavMenu.objects.all()
    context = { "post3": post3 }
    return render(request, template, context)


def NoticiasView(request):
    template_name = 'Noticias.html'
    category = Category.objects.all()
    Filter_Post = request.GET.get('PostFilter', None)
    if Filter_Post:
        listings = Publicación.objects.filter(category__name=Filter_Post, status='publish')
    elif Filter_Post == 'None':
        listings = Publicación.objects.filter(status='publish')
    else:
        listings = Publicación.objects.filter(status='publish')

    context = { 'category': category, 'listings':listings }
    return render(request, template_name, context)

def CategoryView(request, cats):
    template_name = 'category.html'
    category_post = Publicación.objects.filter(category__slug=cats, status='publish')
    context = {'category': cats, 'category_post': category_post}
    return render(request, template_name, context)


def postdetail(request, post):
    template_name = 'single.html'
    post = get_object_or_404(Publicación, slug=post, status='publish') 
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

    context = {'post': post, 'comment': comment,'comment_form': comment_form}
    return render(request, template_name, context)




def  registerView(request):
    template_name =  "registration/register.html"
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserRegistrationForm()

    context={"form": form}
    return render (request, template_name ,context)



def Quienes_somos(request):
    return render(request, "social/Quienes_somos.html")




def NavBare(request):
    template_name = 'navbar.html'
    caters = Category.objects.all()
    context = { 'caters': caters }
    return render(request, template_name, context)
