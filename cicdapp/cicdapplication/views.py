from django.shortcuts import render, HttpResponse

def index(request):
    # Obtener el host desde la cabecera HTTP
    host = request.get_host()
    return HttpResponse(f"repaso testing prueba 16-12-2024 AMI load balancer - Host: {host} ")
