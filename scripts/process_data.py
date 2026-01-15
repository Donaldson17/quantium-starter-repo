import pandas as pd
import glob

# Read all CSV files
dfs = [pd.read_csv(f) for f in glob.glob('data/daily_sales_data_*.csv')]
df = pd.concat(dfs, ignore_index=True)

# Filter for pink morsels only
df = df[df['product'].str.lower() == 'pink morsel']

# Calculate sales (price * quantity)
df['price'] = df['price'].str.replace('$', '').astype(float)
df['sales'] = df['price'] * df['quantity']

# Select columns in the required order
df = df[['sales', 'date', 'region']]

# Save to processed folder with proper headers
df.to_csv('data/processed/pink_morsels_sales.csv', index=False, header=['sales', 'date', 'region'])
print(f"Processed {len(df)} rows")
