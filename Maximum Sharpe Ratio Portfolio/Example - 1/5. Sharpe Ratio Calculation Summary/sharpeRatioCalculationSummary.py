import pandas as pd

# Create a DataFrame
data = {
    'Metric': ['Expected Return', 'Risk-Free Rate', 'Standard Deviation', 'Sharpe Ratio'],
    'Value': [0.10, 0.03, 0.10, 0.70]
}

df = pd.DataFrame(data)
print(df)
