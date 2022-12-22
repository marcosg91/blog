from django.urls import path
from blog import views

#from django.contrib.auth import views as auth_views
#from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView,LogoutView
from blog.forms import UserLoginForm

urlpatterns = [
    path('', views.HomeView, name="home"),
    path('Noticias/',views.NoticiasView,name="noticias_url"),
    path('Nosotros/',views.Quienes_somos,name="nosotros"),
    path('Contactos/',views.contactos,name="contactos"),
    
    path('login/', LoginView.as_view(template_name= "registration/login.html", authentication_form= UserLoginForm), name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/', LogoutView.as_view(next_page='home'),name="logout"),
    
    path('<slug:post>/', views.postdetail, name='post_detail'),
    path('category/<str:cats>/', views.CategoryView, name='categorys_url'),
]

#,authentication_form=UserLoginForm