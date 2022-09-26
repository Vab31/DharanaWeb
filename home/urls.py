from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views
# from django.contrib.auth import views as
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.index, name='home'),
    path('page/<slug:title_name>', views.page,name='page'),
    # path('about',views.about,name='about'),
    
    # path('policy',views.policy,name='policy'),
   
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='create account'),
    path('login',views.handellogin,name='login'),
    path('logout',views.handellogout,name='logout'),
    path('search',views.search,name='search'),
    path('about',views.about,name='aboutus'),
    path('reset_password/',auth_views.PasswordResetView.
    as_view(template_name="password_reset.html")
    ,name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.
    as_view(template_name="password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView
    .as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.
    as_view(template_name="password_reset_done.html"),name="password_reset_complete"),

]
