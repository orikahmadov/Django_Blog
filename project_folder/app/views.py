from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app/base.html", {})




def contact(request):
    return render(request, "app/contact.html")


