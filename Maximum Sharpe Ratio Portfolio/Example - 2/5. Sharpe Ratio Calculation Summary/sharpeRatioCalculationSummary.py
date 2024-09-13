import pandas as pd

# Create a DataFrame
data = {
    'Metric': ['Expected Return', 'Risk-Free Rate', 'Standard Deviation', 'Sharpe Ratio'],
    'Value': [0.09, 0.04, 0.067, 0.746]
}

df = pd.DataFrame(data)
print(df)
