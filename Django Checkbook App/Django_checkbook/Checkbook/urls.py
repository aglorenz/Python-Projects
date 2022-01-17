from django.urls import path
from Checkbook.views import create_account, balance, transaction, index


urlpatterns = [
    path('', index, name='index'),
    path('create/', create_account, name='create'),
    path('<int:pk>/balance/', balance, name='balance'),
    path('transaction/', transaction, name='transaction')
]