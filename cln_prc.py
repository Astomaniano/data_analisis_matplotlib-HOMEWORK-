import pandas as pd

df = pd.read_csv('prices.csv')

df['Price'] = df['Price'].str.replace('руб.', '').str.replace(' ', '').astype(int)

df.to_csv('cleaned_prices.csv', index=False)