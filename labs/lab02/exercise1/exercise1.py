# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    
    round_trip_costs = (((one_way_km * 2) / km_per_liter) * price_per_liter)
    if (budget >= round_trip_costs):
        away = True
    else:
        away = False
    return away

# Test your code here
result = is_budget_sufficient(20,10,20,100)
print(f"Testing Road Trip Budgeter: {result}")


