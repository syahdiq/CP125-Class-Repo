
def filter_query_times(query_times):
   count = len(query_times)
   total = 0
   mean = 0
   total_variance = 0

   for element in query_times:
      total += element

   mean = total / count

   for element in query_times:
      variance_plus = element - mean
      total_variance += variance_plus

   variance = (total_variance ** 2) / count

   std_dev = variance ** 0.5

   upper_limit = mean + std_dev

   for element in query_times:
      if element > upper_limit:
         query_times.remove(element)

   return query_times.sort()

    

# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
