import pandas as pd

data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Chennai', 'Coimbatore', 'Chennai', 'Madurai', 'Coimbatore'],
    'bedrooms': [2, 3, 4, 3, 5],
    'area_sqft': [900, 1200, 1800, 1500, 2200],
    'listing_price': [4500000, 6000000, 9500000, 7000000, 12000000]
}

property_data = pd.DataFrame(data)

# 1. Average listing price by location
avg_price_location = property_data.groupby('location')['listing_price'].mean()
print("Average Listing Price by Location:")
print(avg_price_location)

# 2. Largest property (by area)
largest_property = property_data.loc[property_data['area_sqft'].idxmax()]
print("\nLargest Property:")
print(largest_property)

# 3. Properties with more than 3 bedrooms
more_than_3_bedrooms = property_data[property_data['bedrooms'] > 3]
print("\nProperties with more than 3 bedrooms:")
print(more_than_3_bedrooms)

# 4. Most expensive property
most_expensive = property_data.loc[property_data['listing_price'].idxmax()]
print("\nMost Expensive Property:")
print(most_expensive)