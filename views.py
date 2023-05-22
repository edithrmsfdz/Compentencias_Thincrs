from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
def index (request):

    return HttpResponse('Edith Ramos Fernandez')

class Inicio(View):
    template_name ="index.html"
    
    def post(self,request):
        return render(request)
    
    def get(self,request):
        nombre = 'Edith Ramos'
        edad = 28

        return render(request,self.template_name,{
            'nombre': nombre,
            'edad': edad
                        
        })
    
    

