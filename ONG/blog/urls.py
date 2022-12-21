from blog import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path("", views.HomeView, name="home"),
    path("Quienes_somos/",views.Quienes_somos,name="Quienes_somos"),
    
    path("login/",LoginView.as_view(template_name = "registration/login.html"),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
    
    path('<slug:post>/', views.postdetail, name='post_detail'),
    path('category/<str:cats>/', views.CategoryView, name='categorys'),
]

#,authentication_form=UserLoginForm