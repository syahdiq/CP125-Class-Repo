def withdraw(accounts, card_number, amount):
    # Check if card exists
    if card_number not in accounts:
        return "Card Not Found"

    # Check if balance is sufficient
    if accounts[card_number] < amount:
        return "Insufficient Funds"

    # Deduct amount and update balance
    accounts[card_number] -= amount

    # Return updated balance
    return float(accounts[card_number])

    





accounts = {
    "4111-1111": 500.00,
    "4222-2222": 80.00,
}
print(withdraw(accounts, "4111-1111", 200.00))
print(withdraw(accounts, "4222-2222", 100.00))
print(withdraw(accounts, "9999-0000", 50.00))
