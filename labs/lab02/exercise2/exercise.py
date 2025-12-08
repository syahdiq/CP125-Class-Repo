# Lab 02 Exercise 2: Camping Logistics
# Write your code below:



def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    if participants == 0:
        return 0
    
    if participants % tent_capacity == 0:
        tent_num = participants / tent_capacity
    else:
        tent_num = (participants / tent_capacity) + 1

    total_cost = (tent_price * tent_num) + (meal_price * participants)
    return total_cost
    


result = calculate_event_cost(1,4,30,20)
print(f"Testing Camping Logistics: RM {result}")

