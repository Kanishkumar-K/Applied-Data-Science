import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_csv('house_price_dataset_of_india.csv')

# Descriptive Statistics
# Calculate descriptive statistics
descriptive_stats = df.describe()
print(descriptive_stats)