from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login_page'),
    path('logout/',views.logout_user,name='logout'),
]
