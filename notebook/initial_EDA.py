import pandas as pd
import numpy as np

df = pd.read_csv('../data/your_dataset_file.csv')  # replace with actual filename

df.head()

df.info()  # shows number of non-null entries, data types

df.describe()

missing_counts = df.isnull().sum()
missing_counts[missing_counts > 0]  # show only columns with missing values

duplicate_rows = df[df.duplicated()]
print(f"Number of duplicate rows: {duplicate_rows.shape[0]}")
duplicate_rows.head()  # see examples

print(df['StockCode'].nunique())  # unique product codes
print(df['ProductDescription'].nunique())  # unique descriptions

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
print(df['InvoiceDate'].min(), df['InvoiceDate'].max())

print(df['Quantity'].min(), df['Quantity'].max())
negative_quantities = df[df['Quantity'] < 0]
print(negative_quantities.head())

print(df['Price'].min(), df['Price'].max())
invalid_prices = df[df['Price'] <= 0]
print(invalid_prices.head())

dq_issues = pd.DataFrame({
    'Column': ['CustomerID', 'Quantity', 'InvoiceNo', 'StockCode'],
    'Issue': ['Missing values', 'Negative values', 'Duplicates', 'Inconsistent codes'],
    'Count/Example': [df['CustomerID'].isnull().sum(), 
                       df[df['Quantity']<0].shape[0],
                       df[df.duplicated()]['InvoiceNo'].count(),
                       df['StockCode'].nunique()]
})
dq_issues

