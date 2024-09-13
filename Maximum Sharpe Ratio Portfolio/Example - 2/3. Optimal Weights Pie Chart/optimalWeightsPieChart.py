import matplotlib.pyplot as plt

# Define the weights
weights = [0.55, 0.26, 0.19]
assets = ['Asset X', 'Asset Y', 'Asset Z']

# Create a pie chart
plt.pie(weights, labels=assets, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Optimal Weights for Maximum Sharpe Ratio Portfolio')
plt.show()
