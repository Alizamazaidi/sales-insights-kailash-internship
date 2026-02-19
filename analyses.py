import pandas as pd

# Load the data
df = pd.read_csv("data.csv")

# Preview
print("First 5 rows:")
print(df.head())

# Create revenue column
df["revenue"] = df["unit_price"] * df["quantity"]

# Total revenue
total_revenue = df["revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Product-wise revenue
product_revenue = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Product:")
print(product_revenue)

# Location-wise revenue (NCR)
location_revenue = df.groupby("location")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by NCR Location:")
print(location_revenue)

# Monthly sales trend
df["order_date"] = pd.to_datetime(df["order_date"])
monthly_sales = df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

# Low-performing products
average_revenue = product_revenue.mean()
low_performing_products = product_revenue[product_revenue < average_revenue]
print("\nLow Performing Products:")
print(low_performing_products)
