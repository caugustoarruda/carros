from django.http import HttpResponse

def cars_view(request):
    html = """
        <html>
            <head>
                <title>Carros novos</title>
            </head>
            <body>
                <h1>Aqui voce encontra os carros mais novos da região</h1>
            </body>
        </html>
    """
    return HttpResponse(html)
