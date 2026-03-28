import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

print(orders.head())

print(orders.info())
print(orders.describe())

data = orders.merge(customers, on="customer_id")
data = data.merge(products, on="product_id")

print(data.head())

data["revenue"] = data["quantity"] * data["selling_price_x"]


import matplotlib.pyplot as plt

data["order_date"] = pd.to_datetime(data["order_date"])
data["month"] = data["order_date"].dt.to_period("M")

monthly_sales = data.groupby("month")["revenue"].sum()

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.show()

city_sales = data.groupby("city")["revenue"].sum()

city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.show()

data["month_num"] = data["order_date"].dt.month

from sklearn.linear_model import LinearRegression

X = data[["month_num"]]
y = data["revenue"]

model = LinearRegression()
model.fit(X, y)

future_months = pd.DataFrame({"month_num": [1,2,3,4,5,6]})

predictions = model.predict(future_months)

print(predictions)

plt.plot(future_months["month_num"], predictions)
plt.title("Future Sales Prediction")
plt.show()