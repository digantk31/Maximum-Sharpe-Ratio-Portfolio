import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the covariance matrix
Sigma = np.array([
    [0.0064, 0.00048, 0.00144],
    [0.00048, 0.0144, 0.00144],
    [0.00144, 0.00144, 0.04]
])

# Create a heatmap
sns.heatmap(Sigma, annot=True, cmap='coolwarm', fmt='.4f', 
            xticklabels=['Asset X', 'Asset Y', 'Asset Z'],
            yticklabels=['Asset X', 'Asset Y', 'Asset Z'])
plt.title('Covariance Matrix')
plt.show()
