import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
'Area': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800],
'Price': [20, 25, 32, 38, 42, 48, 55, 62]
}

df = pd.DataFrame(data)

X = df[['Area']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predicted Prices:", predictions.round(2))
print("Mean Absolute Error:", round(mean_absolute_error(y_test, predictions), 2))

area = pd.DataFrame({'Area': [1600]})
predicted_price = model.predict(area)

print("Predicted price for a 1600 sq. ft. house:",
round(predicted_price[0], 2), "Lakhs")
