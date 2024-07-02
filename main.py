import csv


class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    def add_money(self, amount):
        self.balance += amount

    def substract_money(self, amount):
        self.balance -= amount

    def add_transaction(self, date, narrative, amount, paid): # if paid is True -> person sent amount
                                                               # if paid is False -> person received amount
        self.transactions.append((date, narrative, amount, paid))
        self.transactions.sort()

    def __str__(self):
        if self.balance >= 0:
            return "Name: " + self.name + "\nhas money : " + str(self.balance) + "\n"
        else:
            return "Name: " + self.name + "\nhas debt of : " + str(abs(self.balance)) + "\n"

accounts = []


def find_account(acc_name):
    for acc in accounts:
        if acc.name == acc_name:
            return acc
    return False


with open('Transactions2014.csv', newline='') as csvfile:
    csvinfo = csv.reader(csvfile, delimiter=',', quotechar='|')

    first = True

    for row in csvinfo:
        # print(row)
        if first is True:
            first = False
            continue

        # Substract money from sender
        acc_from = find_account(row[1])
        if acc_from != False:
            acc_from.substract_money(float(row[4]))
        else:
            acc_from = Account(row[1])
            accounts.append(acc_from)
            acc_from.substract_money(float(row[4]))

        # Add money to receiver
        acc_to = find_account(row[2])
        if acc_to != False:
            acc_to.add_money(float(row[4]))
        else:
            acc_to = Account(row[2])
            accounts.append(acc_to)
            acc_to.add_money(float(row[4]))

        # Add transaction to each account
        acc_from.add_transaction(row[0], row[3], row[4], True)
        acc_to.add_transaction(row[0], row[3], row[4], False)


    csvfile.close()

for acc in accounts:
    print(acc)