#from django.shortcuts import render
from django.http import HttpResponse

def page1 (request):
    x = """
<html>
    <head></head>
    <body>
        <div style="font-size: 30px; font-weight: 700; color: #aa0000;text-align: center;">
            Page1 text
        </div>
    </body>
</html>

"""
    return HttpResponse(x)

def page2 (request):
    x = "My app page " + "2"
    return HttpResponse(x)

def main (request):
    x = "Index app page"
    return HttpResponse(x)
