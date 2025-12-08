# Lab 02 Exercise 2: Camping Logistics
# Write your code below:



def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    tent_num = tent_capacity / participants
    total_cost = (tent_price * tent_num) + (meal_price * participants)
    return total_cost
    


result = calculate_event_cost(20,4,30,20)
print(f"Testing Camping Logistics: RM {result}")

