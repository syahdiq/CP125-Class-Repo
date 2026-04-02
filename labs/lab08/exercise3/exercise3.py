# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

import csv

def calculate_order_total(products_file, order_file, output_file):
    # Read products file
    f = open(products_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)  # skip header

    prices = {}
    for row in reader:
        product_id = row[0]
        price = float(row[2])
        prices[product_id] = price
    f.close()

    # Read order file
    f = open(order_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)  # skip header

    totals = []
    grand_total = 0

    for row in reader:
        product_id = row[0]
        quantity = int(row[1])

        total_cost = prices[product_id] * quantity
        grand_total += total_cost

        totals.append([product_id, f"{total_cost:.2f}"])
    f.close()

    # Write output
    f = open(output_file, "w", newline="")
    writer = csv.writer(f)

    writer.writerow(["product_id", "total_cost"])
    writer.writerows(totals)

    f.close()

    return grand_total


# Test your code here
result = calculate_order_total(
    "labs/lab08/exercise3/data/products.csv",
    "labs/lab08/exercise3/data/order.csv",
    "labs/lab08/exercise3/data/total.csv"
)
print(f"Grand total: ${result:.2f}")
