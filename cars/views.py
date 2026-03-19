from django.shortcuts import render

def cars_view(request):
    return render(
        request=request, 
        template_name='cars.html',
        context={'cars': {'model': 'Argo 1.0'}}
    )
