
def find_largest_drop(readings):
   drop_list = []
   max = 0
   for i in range(len(readings) - 1):
      prev_reading = readings[i]
      curr_reading = readings[i + 1]
      drop = prev_reading - curr_reading

      if drop > max:
         max = drop
      if max == 0:
       return 0.0
      
   return max
         


         
    
      


# Test
readings = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(readings)
print(f"Largest Drop: {result}")  # Expected: 3.5
