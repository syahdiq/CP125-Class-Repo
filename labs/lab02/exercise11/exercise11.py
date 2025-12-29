
def is_valid_multiple(amount):
    if amount % 10 == 0:
        return True
    else:
        return False

def is_balance_sufficient(amount, balance):
   if balance >= amount:
       return True
   else:
       return False
def process_withdrawal(amount, balance):
    if is_valid_multiple == False:
        print ("Insufficient amount")
    elif is_balance_sufficient:
        print ("Insufficient fund")
    else:
        print ("Successful withdrawal")
