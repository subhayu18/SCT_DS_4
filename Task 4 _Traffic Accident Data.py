# Task 4: Traffic Accident Data Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample accident dataset
data = {
    'time_of_day': ['Morning', 'Evening', 'Night', 'Afternoon', 'Night', 'Morning', 'Evening', 'Night', 'Afternoon', 'Morning'],
    'weather': ['Clear', 'Rainy', 'Fog', 'Clear', 'Rainy', 'Fog', 'Clear', 'Clear', 'Rainy', 'Rainy'],
    'road_condition': ['Dry', 'Wet', 'Wet', 'Dry', 'Wet', 'Wet', 'Dry', 'Dry', 'Wet', 'Wet'],
    'severity': [2, 3, 4, 1, 3, 2, 1, 4, 3, 3]
}

df = pd.DataFrame(data)

# Countplot: Accidents by time of day
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='time_of_day')
plt.title("Accidents by Time of Day")
plt.tight_layout()
plt.show()

# Countplot: Accidents by weather condition
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='weather')
plt.title("Accidents by Weather")
plt.tight_layout()
plt.show()

# Boxplot: Severity vs Road Condition
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='road_condition', y='severity')
plt.title("Severity by Road Condition")
plt.tight_layout()
plt.show()

# Heatmap for correlation (numerical fields only)
df_encoded = df.copy()
df_encoded['severity'] = df_encoded['severity'].astype(float)
df_encoded['is_rainy'] = df['weather'].apply(lambda x: 1 if x == 'Rainy' else 0)
df_encoded['is_wet'] = df['road_condition'].apply(lambda x: 1 if x == 'Wet' else 0)

plt.figure(figsize=(6, 4))
sns.heatmap(df_encoded[['severity', 'is_rainy', 'is_wet']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Severity vs Conditions)")
plt.tight_layout()
plt.show()