"""page_of_memories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Register , name = "Register"),
    path('profile', views.profile , name = "profile"),
    path('logout', views.logout , name = "logout"),
    path('login/', views.Login , name = "login"),
    path('home', views.home , name = "home"),
    path('Addpost', views.Addpost , name = "Addpost"),
    path('viewpost/', views.viewpost , name = "viewpost"),
    path('updatepost/<str:id>/', views.updatepost , name = "updatepost"),
    path('editpost', views.editpost , name = "editpost"),
    path('Deletepost/<str:id>/', views.Deletepost , name = "Deletepost"),
    path('Aboutus', views.Aboutus , name = "Aboutus"),
    path('mydairy/', views.View_Persnol_Dairy , name = "mydairy"),
    path('printpdf/' , views.render_pdf_view , name="printpdf"),
    # path('reset_password/' , auth_views.PasswordResetView.as_view() , name = 'reset_password'),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done" ),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view() , name  = "password_reset_confirm"),
    # path('reset_password_complete/',auth_views.PasswordResetView.as_view() , name ="password_reset_complete" ),

    path('forget-password/', views.ForgetPassword , name="forget-password"),
    path('change-password/<token>/' , views.ChangePassword , name = "change-password"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

