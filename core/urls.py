from django.contrib import admin
from django.urls import path , include
from django.contrib.auth.views import LoginView
from .views import Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('apps.urls')),
    path('login/', LoginView.as_view() , name='login'),
    path('logout/', Logout.as_view() , name='logout'),
]
