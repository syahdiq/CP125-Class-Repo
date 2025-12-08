# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type == "Electric":
        hourly_rate = 2.00
    elif vehicle_type == "Hybrid":
        if (hour_24 >= 6 and hour_24 <= 22):
            hourly_rate = 2.00
        else:
            hourly_rate = 5.00
    else:
        hourly_rate = 5.00
    return hourly_rate

result = get_hourly_rate("Electric" , 11)
print(f"Testing Dynamic Parking Rate: RM {result}")
