from django.urls import path
from . import views

urlpatterns = [
    path('movies/',views.movies,name = 'movies'),
    path('signup/',views.signup,name = 'signup'),
    path('series/',views.series,name = 'series'),
    path('anime/',views.anime,name = 'anime'),
    path('options/',views.options,name = 'options'),
    path('',views.landing,name = 'landing'),
    path('loginform/',views.loginform,name = 'loginform'),
]