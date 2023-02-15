from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import CustomUser, Expert
from .forms import CustomUserCreationForm, ExpertForm
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("This is our homepage! It works!")

class CustomUserSignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Account created successfully')
        return response

class ExpertFormView(CreateView):
    model = Expert
    form_class = ExpertForm
    template_name = 'registration/expert_signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully')
        return response