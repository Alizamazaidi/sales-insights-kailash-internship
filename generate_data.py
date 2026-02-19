import pandas as pd
import random
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(42)

# Sample values
customers = [
    "Aarav Sharma", "Rohit Verma", "Neha Singh", "Priya Gupta", "Kunal Mehta",
    "Ankit Yadav", "Sakshi Jain", "Vikram Malhotra", "Pooja Aggarwal", "Riya Kapoor",
    "Mohit Bansal", "Nitin Arora", "Simran Kaur", "Aman Khanna", "Deepak Chauhan",
    "Ishita Goyal", "Saurabh Mishra", "Naveen Tyagi", "Kritika Goel", "Harsh Vardhan",
    "Aditya Saxena", "Nisha Pandey", "Rahul Tiwari", "Sneha Malhotra", "Varun Ahuja",
    "Akash Tripathi", "Manish Rawat", "Ritu Sharma", "Siddharth Jain", "Tanya Arora"
]

locations = ["Delhi", "Noida", "Gurugram", "Faridabad", "Ghaziabad"]

products = [
    ("Shampoo", "Personal Care", 299),
    ("Facewash", "Personal Care", 199),
    ("Hair Oil", "Personal Care", 249),
    ("Body Lotion", "Personal Care", 349),
    ("Conditioner", "Personal Care", 279),
    ("Soap", "Personal Care", 99),
]

sales_reps = ["Amit", "Rahul", "Neha", "Priya", "Karan", "Ankit"]

start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 7, 31)

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

rows = []
num_rows = 250  # change this to 200+ if you want (e.g., 300)

for i in range(1, num_rows + 1):
    product, category, price = random.choice(products)
    quantity = random.randint(1, 5)
    row = {
        "order_id": 1000 + i,
        "order_date": random_date(start_date, end_date).strftime("%Y-%m-%d"),
        "location": random.choice(locations),
        "customer": random.choice(customers),
        "product": product,
        "category": category,
        "unit_price": price,
        "quantity": quantity,
        "sales_rep": random.choice(sales_reps)
    }
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv("data.csv", index=False)

print("✅ data.csv generated with", num_rows, "rows")
