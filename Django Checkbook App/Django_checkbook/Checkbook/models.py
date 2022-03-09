from django.db import models


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # A model's manager is an object through which Django models perform database queries. Each Django model has at
    # least one manager, and you can create custom managers in order to customise database access
    Accounts = models.Manager()

    # Allows references to a specific account be returned
    # as the owner's name instead of  the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name


TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

# When using modelforms, Django uses foreign key to gather all possible account table id's and translate
# them to "first_name last_name" using the overridden  __str__ dunder method and then display them as a drop down list
# in the web form.  To prevent the "--------" from appearing in the drop down list,  put default='' on the account
# foreign key field of the Transaction class.


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default='')  # remove "-------" from acct drop down
    # by using  default=''

    # A model's manager is an object through which Django models perform database queries. Each Django model has at
    # least one manager, and you can create custom managers in order to customise database access
    Transactions = models.Manager()
