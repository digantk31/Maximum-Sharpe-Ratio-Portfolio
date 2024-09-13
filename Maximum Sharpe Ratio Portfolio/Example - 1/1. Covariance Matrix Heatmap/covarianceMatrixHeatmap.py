import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the covariance matrix
Sigma = np.array([
    [0.01, 0.009],
    [0.009, 0.0225]
])

# Create a heatmap
sns.heatmap(Sigma, annot=True, cmap='coolwarm', fmt='.4f', 
            xticklabels=['Asset A', 'Asset B'],
            yticklabels=['Asset A', 'Asset B'])
plt.title('Covariance Matrix')
plt.show()
