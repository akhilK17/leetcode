import pandas as pd
from datetime import timedelta
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('TSLA.csv')

# Parse the date column
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# Create numerical columns for regression
data['Date_ordinal'] = data['Date'].map(pd.Timestamp.toordinal)

# Split the data into training and testing sets
train_data = data[data['Date'] < data['Date'].max() - timedelta(days=365)]
test_data = data[data['Date'] >= data['Date'].max() - timedelta(days=365)]

# Prepare the training and testing data
X_train = train_data[['Date_ordinal']]
y_train_close = train_data['Close']
y_train_volume = train_data['Volume']

X_test = test_data[['Date_ordinal']]
y_test_close = test_data['Close']
y_test_volume = test_data['Volume']

# Train the linear regression models
model_close_train = LinearRegression()
model_close_train.fit(X_train, y_train_close)

model_volume_train = LinearRegression()
model_volume_train.fit(X_train, y_train_volume)

# Make predictions on the test data
y_pred_close = model_close_train.predict(X_test)
y_pred_volume = model_volume_train.predict(X_test)

# Calculate evaluation metrics
mse_close = mean_squared_error(y_test_close, y_pred_close)
r2_close = model_close_train.score(X_test, y_test_close)

mse_volume = mean_squared_error(y_test_volume, y_pred_volume)
r2_volume = model_volume_train.score(X_test, y_test_volume)

# Plot the results
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot Close price and its trend
ax1.plot(train_data['Date'], train_data['Close'], label='Train Close Price', color='blue')
ax1.plot(test_data['Date'], test_data['Close'], label='Test Close Price', color='blue', linestyle=':')
ax1.plot(test_data['Date'], y_pred_close, label='Predicted Close Price', color='red', linestyle='--')
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.legend(loc='upper left')

# Create a second y-axis for Volume
ax2 = ax1.twinx()
ax2.plot(train_data['Date'], train_data['Volume'], label='Train Volume', color='green')
ax2.plot(test_data['Date'], test_data['Volume'], label='Test Volume', color='green', linestyle=':')
ax2.plot(test_data['Date'], y_pred_volume, label='Predicted Volume', color='orange', linestyle='--')
ax2.set_ylabel('Volume', color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.legend(loc='upper right')

plt.title('TSLA Price and Volume Trends - Model Testing')
plt.show()

# Print evaluation metrics
print(f'MSE Close: {mse_close}, R^2 Close: {r2_close}')
print(f'MSE Volume: {mse_volume}, R^2 Volume: {r2_volume}')
