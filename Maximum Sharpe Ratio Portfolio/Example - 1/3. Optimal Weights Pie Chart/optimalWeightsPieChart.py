import matplotlib.pyplot as plt

# Define the weights
weights = [0.50, 0.50]
assets = ['Asset A', 'Asset B']

# Create a pie chart
plt.pie(weights, labels=assets, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Optimal Weights for Maximum Sharpe Ratio Portfolio')
plt.show()
