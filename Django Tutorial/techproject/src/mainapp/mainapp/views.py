from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    context = {
        'products': products
    }
    return render(request, "home.html", context)
    # return render(request, "home.html") # this will work, too, if you don't have data to pass.

    # user = request.user
    # context = {
    #     'user': user,
    # }
    # # return HttpResponse("<h1>Welcome {}!</h1>".format(user))
    # return render(request, "home.html", context)