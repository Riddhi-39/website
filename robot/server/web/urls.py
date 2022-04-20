"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("base/", base, name="base"),
    path("faq/", faq, name="faq"),
    path("about-us/", about, name="about"),
    path("team/", team, name="team"),
    path("privacy/", privacy, name="privacy"),
    path("contact-us/", contact, name="contact"),
    path("software-download/", download, name="download"),
    path("coming-soon/", comingsoon, name="comingsoon"),
    path("error/", error, name="error"),
    path("mobile-app/", mobile, name="mobile"),
    path("software-demo/", software, name="software"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("chatbot/", chatbot, name="chatbot"),
    path("nlp/", nlp, name="nlp"),
]
