from django.shortcuts import render 

def inicio(request):
    template_name = "publicaciones/index.html"
    contexto = {
        
    }
    return render( request, template_name, contexto)