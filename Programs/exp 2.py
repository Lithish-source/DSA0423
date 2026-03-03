import pandas as pd

data = {
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2026-01-10', '2026-01-12', '2026-01-15',
                   '2026-01-20', '2026-01-25', '2026-02-01'],
    'product_name': ['Laptop', 'Mobile', 'Tablet',
                     'Laptop', 'Tablet', 'Mobile'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
}

order_data = pd.DataFrame(data)

order_data['order_date'] = pd.to_datetime(order_data['order_date'])

orders_per_customer = order_data.groupby('customer_id').size()
print("Total Orders per Customer:")
print(orders_per_customer)

avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
print("\nAverage Order Quantity per Product:")
print(avg_quantity_per_product)

earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)