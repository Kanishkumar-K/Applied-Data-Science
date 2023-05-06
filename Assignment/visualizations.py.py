# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Download the dataset from Kaggle
# Dataset Link: https://www.kaggle.com/datasets/mohamedafsal007/house-Price-dataset-of-india
# Load the dataset into a pandas dataframe
df = pd.read_csv('house_Price_dataset_of_india.csv')

# Univariate Analysis

# Plot a histogram of the house Price
sns.histplot(df['Price'])
plt.title('Distribution of House Price')
plt.show()

# Plot a boxplot of the house Price
sns.boxplot(df['Price'])
plt.title('Boxplot of House Price')
plt.show()

# Plot a kernel density estimation (KDE) plot of the house Price
sns.kdeplot(df['Price'])
plt.title('KDE Plot of House Price')
plt.show()

# Bivariate Analysis

# Plot a scatter plot of square feet vs. Price
sns.scatterplot(x='number of bathrooms', y='Price', data=df)
plt.title('Scatter Plot of Square Feet vs. Price')
plt.show()

# Plot a line plot of bedrooms vs. Price
sns.lineplot(x='number of bedrooms', y='Price', data=df)
plt.title('Line Plot of Bedrooms vs. Price')
plt.show()

# Plot a heatmap of the correlation between the variables
sns.heatmap(df.corr(), annot=True)
plt.title('Heatmap of Correlation between Variables')
plt.show()

# Multivariate Analysis

# Plot a pair plot of selected variables
sns.pairplot(df, vars=[ 'number of bedrooms', 'number of bathrooms', 'Price','living area'])
plt.title('Pair Plot of Selected Variables')
plt.show()

# Plot a cluster map of the correlation between the variables
sns.clustermap(df.corr())
plt.title('Cluster Map of Correlation between Variables')
plt.show()
