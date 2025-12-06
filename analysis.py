# Data Analysis for E-commerce
# Submitted by: 22f3000162@ds.study.iitm.ac.in

import pandas as pd

data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Value': [65.36, 73.72, 75.96, 75.3]
}

df = pd.DataFrame(data)
average = df['Value'].mean()
print(f"Average: {average:.2f}")
print("Recommendation: implement targeted retention campaigns")
