from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {}
    return render(request, "core/index.html", context)


def aboutpage(request):
    context = {}
    return render(request, "core/about.html", context)


def blog(request):
    context = {}
    return render(request, "core/blog.html", context)


def product(request):
    context = {}
    return render(request, "core/products.html", context)


def contact(request):
    context = {}
    return render(request, "core/contact.html", context)