import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Download the dataset from Kaggle
# Dataset Link: https://www.kaggle.com/datasets/mohamedafsal007/house-Price-dataset-of-india
# Load the dataset into a pandas dataframe
df = pd.read_csv('house_price_dataset_of_india.csv')
print('Shape of dataframe before dropping missing values:', df.shape)

# Drop the missing values
df = df.dropna()

# Print the shape of the dataframe after dropping the missing values
print('Shape of dataframe after dropping missing values:', df.shape)