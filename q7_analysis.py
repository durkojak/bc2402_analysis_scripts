import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('result of question 7.csv')

grouped_data = df.groupby(['airline', 'class', 'season']).agg({
    'AvgOverallRating': 'mean'
}).reset_index()

sns.set_style("whitegrid")

airlines = grouped_data['airline'].unique()

for airline in airlines:
    plt.figure(figsize=(12, 6))
    sns.barplot(x='class', y='AvgOverallRating', hue='season', data=grouped_data[grouped_data['airline'] == airline], ci=None)
    plt.title(f'Average Overall Rating by Class for {airline}')
    plt.ylabel('Average Overall Rating')
    plt.xlabel('Class')
    plt.xticks(rotation=45)
    plt.legend(title='Season')
    plt.show()

seasonal_comparison_data = df.groupby(['airline', 'season']).agg({
    'AvgOverallRating': 'mean'
}).reset_index()

pivot_data = seasonal_comparison_data.pivot(index='airline', columns='season', values='AvgOverallRating').reset_index()

pivot_data.plot(kind='bar', x='airline', figsize=(14, 8))
plt.title('Average Overall Rating: Seasonal vs Non-Seasonal for Each Airline')
plt.ylabel('Average Overall Rating')
plt.xlabel('Airline')
plt.xticks(rotation=45)
plt.legend(title='Season')
plt.show()

rating_columns = ['AvgSeatComfort', 'AvgFoodnBeverages', 'AvgInflightEntertainment', 'AvgValueForMoney', 'AvgOverallRating']

correlation_matrix = df[rating_columns].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Matrix of Rating Categories')

plt.subplots_adjust(bottom=0.3)

plt.xticks(rotation=0)

plt.show()