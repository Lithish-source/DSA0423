import pandas as pd

# Load dataset
df = pd.read_csv(r"E:\College\DSA0423\Activity 2\Sample - Superstore.csv", encoding='latin1')

# Remove any hidden spaces
df.columns = df.columns.str.strip()

# View dataset
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# 1. Total Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nTotal Sales by Category:")
print(category_sales)


# 2. Total Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region:")
print(region_sales)


# 3. Average Sales per Sub-Category
avg_sales = df.groupby("Sub-Category")["Sales"].mean()
print("\nAverage Sales per Sub-Category:")
print(avg_sales)


# 4. High Sales Transactions
high_sales = df[df["Sales"] > 500]
print("\nHigh Sales Transactions:")
print(high_sales[["Product Name","Sales","Region"]])


# 5. Pivot Table (Region vs Category)
pivot_table = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum"
)

print("\nPivot Table (Region vs Category):")
print(pivot_table)