from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    context = {
        'products': products
    }
    return render(request, "home.html", context)

    # user = request.user
    # context = {
    #     'user': user,
    # }
    # # return HttpResponse("<h1>Welcome {}!</h1>".format(user))
    # return render(request, "home.html", context)