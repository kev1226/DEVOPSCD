from django.shortcuts import render, HttpResponse

def index(request):
    # Obtener el host desde la cabecera HTTP
    host = request.get_host()
    return HttpResponse(f"repaso testing prueba 2.9 load balancer - Host: {host} ")
