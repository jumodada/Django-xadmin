from django.shortcuts import render

# Create your views here.

def messgae_form(request):
    return render(request, "./form.html")