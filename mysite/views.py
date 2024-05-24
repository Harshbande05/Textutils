# This File is created by me -HARSH
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    #Taking input text
    djtext = request.POST.get("text","default")
    removepunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps","off")
    charcount = request.POST.get("charcount","off")

    #check if the option is selected
    if removepunc == "on":
        punctions = """!@#$%^&*()_+:<>?"}{"""
        analyzed = ""
        for i in djtext:
            if i not in punctions:
                analyzed = analyzed + i
        params ={"purpose":"Remove Punction","analyzed_text":analyzed}
        return render(request,"analyze.html",params)
    
    elif fullcaps == "on":
        analyzed = ""
        for i in djtext:
            analyzed = analyzed + i.upper()
        params ={"purpose":"uppercase","analyzed_text":analyzed}
        return render(request,"analyze.html",params)
    
    elif charcount == "on":
        analyzed = 0
        no_spaces = djtext.replace(" ", "")
        djtext = no_spaces
        for i in djtext:
            analyzed = analyzed + 1
        params ={"purpose":"Count characters","analyzed_text":analyzed}
        return render(request,"analyze.html",params)

    else:
        return HttpResponse("ERROR !")