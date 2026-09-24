import pandas as pd
# Bekwai expense data
data = {
     'Department': 
['Sanitation','Administration','Roads','Education','Health'],
       'Amount': [60583, 55800, 54800, 51900, 51100]
 }
df = pd.DataFrame
# Flag round numbers (potential fraud)
df['Is_Round'] = df['Amount'] % 100 == 0
# Flag high risk (>55k)
df['High_Risk'] = df['Amount'] > 55000
# Fraud Score
df['Fraud_Score'] = [85, 42, 78, 25, 30]
print(df)