import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the correlation matrix
Corr = np.array([
    [1, 0.6],
    [0.6, 1]
])

# Create a heatmap
sns.heatmap(Corr, annot=True, cmap='coolwarm', fmt='.2f', 
            xticklabels=['Asset A', 'Asset B'],
            yticklabels=['Asset A', 'Asset B'])
plt.title('Correlation Matrix')
plt.show()
