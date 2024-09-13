import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the correlation matrix
Corr = np.array([
    [1, 0.5, 0.3],
    [0.5, 1, 0.6],
    [0.3, 0.6, 1]
])

# Create a heatmap
sns.heatmap(Corr, annot=True, cmap='coolwarm', fmt='.2f', 
            xticklabels=['Asset X', 'Asset Y', 'Asset Z'],
            yticklabels=['Asset X', 'Asset Y', 'Asset Z'])
plt.title('Correlation Matrix')
plt.show()
