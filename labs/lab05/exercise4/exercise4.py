
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    pass


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
