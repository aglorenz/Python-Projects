from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm


# Create your views here.
def index(request):
    # print("entering Home view")
    form = TransactionForm(data=request.POST or None)
    # print("printing form 1")
    # print(type(form))
    # print(form)
    if request.method == 'POST':
        # print("entering POST")
        pk = request.POST['account']
        return balance(request, pk)
    content = {'form': form}
    # print("Entering Get")
    # print(type(content))
    # print(content)
    # print("Content = {}".format(content))
    # print("printing form2")
    # print(form)
    return render(request, 'checkbook/index.html', content)


def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)


def balance(request, pk):
    # Account is First and Last name concatenated as returned by the def __str__(self): method in models.py
    account = get_object_or_404(Account, pk=pk)
    # Sorting transactions by date like they should be on a register!  :)
    transactions = Transaction.Transactions.all().filter(account=pk).order_by('date')
    current_total = account.initial_deposit

    table_contents = { }
    # create a dictionary of transactions with running total as the value
    for t in transactions:
        print(t)   # t is the primary key reference to the rows belonging to the current account
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    print(table_contents)
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
