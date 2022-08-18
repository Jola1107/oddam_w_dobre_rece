from django.shortcuts import render
from django.views import View

class LandingPageView(View):
    def get(self, request):

        return render(request, "index.html")

class AddDonationView(View):
    def get(self, request):

        return render(request, "form.html")

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", context={"form": form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", context={"form": form})