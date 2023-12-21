from django.urls import path
from .views import Home , TodoAction


urlpatterns = [
    path('' , Home.as_view() , name='home'),
    path('<int:pk>/<str:action>/' , TodoAction.as_view(),name='action'),
]