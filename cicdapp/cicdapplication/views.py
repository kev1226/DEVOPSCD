from django.shortcuts import render, HttpResponse

def index(request):
    # Obtener el host desde la cabecera HTTP
    host = request.get_host()
    return HttpResponse(f"repaso testing prueba load balancer - Host: {host} INSTANCE2")
