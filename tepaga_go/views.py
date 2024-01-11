from django.shortcuts import render, redirect
from . import models
from .forms import ContactForm
# Create your views here.




def index(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    
            form = ContactForm()
        
    advantages = models.Advantage.objects.all()[:3]
    portfolio = models.Portfolio.objects.all()[:3]
    video = models.Video.objects.latest("pk") if models.Video.objects.exists() else []
    blog = models.Blog.objects.all()[:3]
    trip =  models.Trips.objects.latest("pk") if models.Trips.objects.exists() else []
    
    context = {
        "advantages": advantages,
        "portfolio":portfolio,
        "video": video,
        "blogs": blog,
        "trip":trip,
        "form":form 
    }
    
    return render(request, "tepaga_go/index.html", context=context)


def portfolio(request):
    
    portfolio = models.Portfolio.objects.all()
    
    return render(request, "tepaga_go/portfolio.html", context={"portfolio":portfolio})


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect("index")
    trip =  models.Trips.objects.latest("pk") if models.Trips.objects.exists() else []       

    return render(request, "tepaga_go/contact.html", {"form":form, "content":trip})


def blog(request):
    
    blog = models.Blog.objects.all()
    
    return render(request, "tepaga_go/blog.html", context={"blogs":blog})


def detail(request, type, pk):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    
            return redirect("index")
        
    match type:
        case "blog":
            blog = models.Blog.objects.get(pk=pk)
            context = {"content":blog}
        case "portfolio":
            portfolio = models.Portfolio.objects.get(pk=pk)
            context = {"content":portfolio}       
        case "trip":
            trip = models.Trips.objects.get(pk=pk)
            context = {"content":trip}
        
        case _:
            context = {}
        
    context["form"] = form      
    
    
    return render(request, "tepaga_go/detail.html", context=context)
