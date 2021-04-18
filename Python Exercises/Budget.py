
def calcBills():
    myBills = {'Electric': 120.00, 'Rent': 1200.00, 'Water_Sewer': 60.00,
               'Car Insurance': 75.00, 'Phone': 65.00}
    print(type(myBills))
    total = 0
    for i in myBills:
        print(i)
        total += myBills[i]
    owed = 'the total owed for bills this mongth is: ${}'.format(total)
    return owed
    
