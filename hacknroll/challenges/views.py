from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Challenge2Form

def homepage(request):
    return render(request, 'challenges/homepage.html')

class challenge2(LoginRequiredMixin, View):
    def get(self, request):
        form = Challenge2Form()
        return render(request, 'challenges/challenge2.html', {'form': form})
    
    def post(self, request):
        form = Challenge2Form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/c3')                                    
        else:                                        
            return render(request, 'challenges/challenge2.html', {'form': form})

def cookieview(request):
        html = '<html><head><link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"></head><style>body{text-align: center;} .i {text-align:center;}</style><body><i class="fas fa-cookie-bite fa-10x"></i><h2>Get the fortune in this cookie</h2></body></html>'
        response = HttpResponse(html)
        response.set_cookie("fortune", "r0lls0fc4sh4ndb1lls")
        return response

class challenge3(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'challenges/challenge3.html')

class challenge4(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'challenges/challenge4.html')
