from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = ["Andy", "Mark", "Janis", "Kitters", "Vreni"]
    context = {
        "names": names
    }
    return render(request, "home.html", context)

    # user = request.user
    # context = {
    #     'user': user,
    # }
    # # return HttpResponse("<h1>Welcome Awesome {}!".format(user))
    # return render(request, "home.html", context)