import matplotlib.pyplot as plt

# Define the values
metrics = ['Expected Return', 'Standard Deviation']
values = [0.10, 0.10]

# Create a bar chart
plt.bar(metrics, values, color=['#ff9999', '#66b3ff'])
plt.title('Portfolio Metrics')
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.show()
