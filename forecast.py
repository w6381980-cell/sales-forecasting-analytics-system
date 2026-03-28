import pandas as pd
from sklearn.linear_model import LinearRegression

# ----------------------
# Load Data
# ----------------------
orders = pd.read_csv("orders.csv")

# ----------------------
# Prepare Data
# ----------------------
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["month_num"] = orders["order_date"].dt.month

orders["revenue"] = orders["quantity"] * orders["selling_price"]

# ----------------------
# Train Model (IMPORTANT 🔥)
# ----------------------
X = orders[["month_num"]]
y = orders["revenue"]

model = LinearRegression()
model.fit(X, y)

# ----------------------
# Future Prediction
# ----------------------
future_months = pd.DataFrame({
    "month_num": [1,2,3,4,5,6]
})

predictions = model.predict(future_months)

future_months["Predicted_Sales"] = predictions

# ----------------------
# Save Output
# ----------------------
future_months.to_csv("forecast.csv", index=False)

print(" Forecast Generated Successfully!")