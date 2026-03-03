import pandas as pd

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Price': [60000, 20000, 30000, 60000, 20000],
    'Quantity': [2, 5, 3, 1, 4]
}

sales_data = pd.DataFrame(data)

sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

total_sales_per_product = sales_data.groupby('Product')['Total Sales'].sum()

print("Sales Data with Total Sales Column:")
print(sales_data)

print("\nTotal Sales for Each Product:")
print(total_sales_per_product)