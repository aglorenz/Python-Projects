from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    names = ["Andy", "Mark", "Janis", "Kitters", "Vreni"]
    context = {
        "names": names
    }
    return render(request, "index.html", context)

    # user = request.user
    # context = {
    #     'user': user,
    # }
    # # return HttpResponse("<h1>Welcome Awesome {}!".format(user))
    # return render(request, "index.html", context)

def about(request):
    # names = ["Andy", "Mark", "Janis", "Kitters", "Vreni"]
    # context = {
    #     "names": names
    # }
    return render(request, "about.html")