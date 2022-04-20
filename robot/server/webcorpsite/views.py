from django.shortcuts import render

# Create your views here.
# Create your views here.

def base(request):
    return render(request, "base.html")


def index(request):
    return render(request, "index.html")

def faq(request):
    return render(request, "faq.html")

def about(request):
    return render(request, "about-us.html")

def team(request):
    return render(request, "team.html")

def privacy(request):
    return render(request, "privacy.html")

def contact(request):
    return render(request, "contact-us.html")

def download(request):
    return render(request, "software-download.html")

def comingsoon(request):
    return render(request, "coming-soon.html")

def error(request):
    return render(request, "error.html")

def mobile(request):
    return render(request, "mobile-app.html")

def software(request):
    return render(request, "software-demo.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def chatbot(request):
    return render(request, "chatbot.html")

def nlp(request):
    return render(request, "nlp.html")