# Data Analysis for Financial Services

import pandas as pd

data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Value': [223.36, 231.72, 233.96, 233.3]
}

df = pd.DataFrame(data)
average = df['Value'].mean()
print(f"Average: {average:.2f}")
print("Recommendation: optimize digital marketing channels")
