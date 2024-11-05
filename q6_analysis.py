import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('result of question 6.csv')  # updated file path

correlations = df[['LengthOfStay', 'WantsExtraBaggage', 'PrefSeat', 'WantsMeals']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlations, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Length of Stay and Preferences")
plt.show()
