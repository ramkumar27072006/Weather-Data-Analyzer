import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

CSV_FILE = r"E:\DOWNLOAD\DailyDelhiClimateTrain.csv"
df = pd.read_csv(CSV_FILE)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date', 'meantemp', 'humidity', 'wind_speed'])
df.rename(columns={'meantemp': 'temperature'}, inplace=True)
for col in ['temperature', 'humidity', 'wind_speed']:
    df[col] = df[col].fillna(df[col].mean())
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
def get_season(month):
    if month in [12, 1, 2]: return 'Winter'
    if month in [3, 4, 5]: return 'Spring'
    if month in [6, 7, 8]: return 'Summer'
    return 'Fall'
df['season'] = df['month'].apply(get_season)
scaler = MinMaxScaler()
df[['temperature', 'humidity', 'wind_speed']] = scaler.fit_transform(df[['temperature', 'humidity', 'wind_speed']])

valid_years = df['year'].value_counts()
full_years = valid_years[valid_years > 300].index
df_full = df[df['year'].isin(full_years)]

print("\nAnnual Weather Statistics:")
annual_stats = df_full.groupby('year').agg({
    'temperature': ['mean', 'median', 'std'],
    'humidity': 'mean',
    'wind_speed': 'sum'
})
print(annual_stats)
print("\nDescriptive Statistics (Normalized):")
print(df_full[['temperature', 'humidity', 'wind_speed']].describe())
corr = df_full[['temperature', 'humidity', 'wind_speed']].corr()
print("\nCorrelation Matrix:")
print(corr)
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Temperature trend over the years
plt.figure(figsize=(10,6))
yearly_temp = df_full.groupby('year')['temperature'].mean()
plt.plot(yearly_temp.index, yearly_temp, color='red', marker='o', linewidth=2)
plt.title("Temperature Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Average Normalized Temperature")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Monthly Mean Temp
plt.figure(figsize=(10,6))
monthly_temp = df_full.groupby(['year', 'month'])['temperature'].mean().unstack()
monthly_temp.T.plot(ax=plt.gca(), linewidth=2)
plt.title("Monthly Temperature Trends, by Year")
plt.xlabel("Month")
plt.ylabel("Average Normalized Temperature")
plt.legend(title="Year")
plt.tight_layout()
plt.show()

# wind speed 
plt.figure(figsize=(10,6))
yearly_wind = df_full.groupby('year')['wind_speed'].sum()
plt.bar(yearly_wind.index, yearly_wind, color='royalblue', width=0.8)
plt.title("Yearly Wind Speed Distribution")
plt.xlabel("Year")
plt.ylabel("Total Normalized Wind Speed")
plt.tight_layout()
plt.show()

# Humidity vs Temperature
plt.figure(figsize=(7,6))
scatter_df = df_full.sample(n=4000, random_state=42) if len(df_full) > 4000 else df_full
plt.scatter(scatter_df['temperature'], scatter_df['humidity'], s=15, c='purple', alpha=0.5)
plt.title("Humidity vs Temperature Correlation")
plt.xlabel("Normalized Temperature")
plt.ylabel("Normalized Humidity")
plt.tight_layout()
plt.show()

# Linear Regression of Yearly Means
if len(yearly_temp) > 1:
    X = yearly_temp.index.values.reshape(-1,1)
    y = yearly_temp.values
    model = LinearRegression()
    model.fit(X, y)
    future_years = np.arange(X.min(), X.max() + 6).reshape(-1, 1)
    prediction = model.predict(future_years)
    plt.figure(figsize=(10,6))
    plt.scatter(X.flatten(), y, color='blue', s=80, label='Actual')
    plt.plot(future_years.flatten(), prediction, color='orange', linestyle='-', linewidth=2, label='Prediction')
    plt.title("Temperature Prediction for Next Years")
    plt.xlabel("Year")
    plt.ylabel("Average Normalized Temperature")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    mse = mean_squared_error(y, model.predict(X))
    rmse = np.sqrt(mse)
    print("\nLinear Regression Model Evaluation:")
    print(f"Mean Squared Error (MSE): {mse:.6f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.6f}")
    for year, pred in zip(future_years.flatten()[-5:], prediction[-5:]):
        print(f"Predicted avg normalized temperature for {int(year)}: {pred:.3f}")
else:
    print("Not enough years for regression forecasting.")

# Key Insights
max_temp_year = yearly_temp.idxmax()
max_temp_val = yearly_temp.max()
max_wind_year = yearly_wind.idxmax()
max_wind_val = yearly_wind.max()
print("\n--- Key Climate Insights ---")
print(f"Year with highest average temperature: {max_temp_year} ({max_temp_val:.3f})")
print(f"Year with highest total wind speed: {max_wind_year} ({max_wind_val:.3f})")
