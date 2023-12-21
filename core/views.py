from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class Logout(LoginRequiredMixin , View):
    def get(self , request):
        context = {

        }
        return render(request ,'registration/logged_out.html' , context)
