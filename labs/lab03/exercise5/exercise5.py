def get_position(cars, car_number):
    for i in range(len(cars)):
        if cars(i) == car_number:
            return i

def has_overtaken(before, after, car1, car2):
   car1_before = get_position(before, car1)
   car2_before

