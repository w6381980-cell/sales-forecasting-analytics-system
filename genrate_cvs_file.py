import pandas as pd
import numpy as np

# ----------------------
# 1. Customers Data
# ----------------------
customers = pd.DataFrame({
    "customer_id": range(1, 101),
    "customer_name": ["Customer_" + str(i) for i in range(1, 101)],
    "city": np.random.choice(["Mumbai", "Delhi", "Pune", "Nashik"], 100),
    "segment": np.random.choice(["Consumer", "Corporate"], 100)
})

# ----------------------
# 2. Products Data
# ----------------------
products = pd.DataFrame({
    "product_id": range(1, 51),
    "product_name": ["Product_" + str(i) for i in range(1, 51)],
    "category": np.random.choice(["Electronics", "Clothing", "Home"], 50),
    "cost_price": np.random.randint(100, 1000, 50),
})

products["selling_price"] = products["cost_price"] + np.random.randint(50, 300, 50)

# ----------------------
# 3. Orders Data
# ----------------------
orders = pd.DataFrame({
    "order_id": range(1, 1001),
    "customer_id": np.random.choice(customers["customer_id"], 1000),
    "product_id": np.random.choice(products["product_id"], 1000),
    "quantity": np.random.randint(1, 5, 1000),
    "order_date": pd.date_range(start="2023-01-01", periods=1000, freq="D")
})

# Merge price
orders = orders.merge(products[["product_id", "selling_price"]], on="product_id")

# ----------------------
# Save Files
# ----------------------
customers.to_csv("customers.csv", index=False)
products.to_csv("products.csv", index=False)
orders.to_csv("orders.csv", index=False)

print("Dataset Generated Successfully!")