import pandas as pd

# Read the CSV file
df = pd.read_csv('gold_oil_post_covid.csv')

# Convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%b %d %Y')

# Convert the date column to the desired format
df['date'] = df['date'].dt.strftime('%d-%m-%Y')

# Write the modified table to a new CSV file
df.to_csv('post.csv', index=False)