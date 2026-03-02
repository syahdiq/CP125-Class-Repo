# Lab 08 Exercise 5: Sales Summary
# Write your code below:

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    # TODO: Implement this function
    pass


# Test your code here
result = summarize_sales("data/sales.csv", "data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
