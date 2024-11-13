import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('result of question 6.csv')

# Calculate the normalized attributes
df['LengthOfStay'] = df['LengthOfStay'] / df['AverageFlightDuration']
df['PrefSeat'] = df['PrefSeat'] / df['AverageFlightDuration']
df['WantsMeals'] = df['WantsMeals'] / df['AverageFlightDuration']
df['WantsExtraBaggage'] = df['WantsExtraBaggage'] / df['AverageFlightDuration']

# Create scatter plots for each attribute normalized by AverageFlightDuration
attributes = ['LengthOfStay', 'PrefSeat', 'WantsMeals', 'WantsExtraBaggage']
titles = ['Length of Stay', 'Preferred Seat', 'Wants In-Flight Meals', 'Wants Extra Baggage']

for attribute, title in zip(attributes, titles):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='AverageFlightDuration', y=attribute, data=df)
    plt.title(f'Relationship between Average Flight Duration and {title}')
    plt.xlabel('Average Flight Duration (hours)')
    plt.ylabel(title)
    plt.show()

# Calculate the correlation matrix
correlation_matrix = df[attributes].corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Matrix of Normalized Attributes')
plt.show()