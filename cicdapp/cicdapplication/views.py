from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("Cada dia mas devops")