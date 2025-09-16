# Weather Data Analyzer - Arttifai Tech 

---

## Project Aim

This project analyzes multi-year Delhi weather data to uncover climate patterns, visualize temperature and humidity trends, and forecast future temperature using linear regression.

---

## Key Focus Areas

- **Data Collection/Cleaning:** Handle missing data, normalize features, and engineer time-based columns.
- **Exploratory Data Analysis:** Uncover trends and relationships using descriptive statistics and correlation heatmaps.
- **Visualization:** Communicate insights through Matplotlib/Seaborn—line chart, bar graph, scatter plot, regression trend.
- **Predictive Analysis:** Model and forecast average temperature for the next 5 years.
- **Statistical Reporting:** Print yearly and aggregate statistics, as well as model performance metrics.

---

## Project Objectives

**Data Processing & EDA:**
- Load and clean daily weather dataset for Delhi (2013–2016), including:  
  `date`, `temperature`, `humidity`, `wind_speed`
- Fill missing values, normalize features, and extract year/month/season
- Display summary tables, annual weather stats, correlation matrix

**Visualization:**
- **Line Chart:** Average yearly temperature, to show climate trend
- **Bar Graph:** Yearly wind speed totals (since rainfall is not available)
- **Scatter Plot:** Humidity vs. Temperature
- **Monthly Trends Plot:** Monthly temperature curves for each year
- **Correlation Heatmap:** Visual matrix of all key numeric features
- **Forecast Plot:** Linear regression line predicting average temperature for 5 more years (orange line over actual points)

<img width="1000" height="600" alt="TEMP PRED FOR NEXT YEARS" src="https://github.com/user-attachments/assets/c47aaca5-39ea-4258-9a55-867b20d9ab2c" />
<img width="700" height="600" alt="HUMIDITY vs TEMP CORRELATION" src="https://github.com/user-attachments/assets/82142068-dde5-432a-b627-06c7c80e46ec" />
<img width="1000" height="600" alt="YEARLY WIND SPEED DISTRIBUTION" src="https://github.com/user-attachments/assets/7f2644a0-40e5-4610-9bd3-2149fe3b66a7" />
<img width="1000" height="600" alt="MONTHLY TEMP TRENDS, BY YEAR" src="https://github.com/user-attachments/assets/ab017a25-f465-4e3c-9c52-c10f2517653d" />
<img width="1000" height="600" alt="TEMPERATURE TREND over years" src="https://github.com/user-attachments/assets/159a3bac-55b5-4f45-b7d2-79e81f309e5f" />
<img width="600" height="400" alt="CORRELATION HEATMAP" src="https://github.com/user-attachments/assets/b2e6cba3-aa2d-40c6-a6a1-dafe8d212b71" />



**Predictive Modeling:**
- Train linear regression on historical yearly averages
- Display model performance (MSE, RMSE) in console
- Make and print next 5-year predictions

**Statistical Summary:**
- Print summary tables and highlight hottest and windiest years

---

## Dataset Used

- **File:** `DailyDelhiClimateTrain.csv`
- **Source:** [Kaggle: Daily Climate time series data](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data)
- **Columns used:** `date`, `meantemp` (as temperature), `humidity`, `wind_speed`

---

## Installation

1. **Clone this repo:**  
```bash
git clone https://github.com/ramkumar27072006/Weather-Data-Analyzer.git
cd Weather-Data-Analyzer
```

2. **Install Python dependencies:**  
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. **Add dataset:**  
Ensure `DailyDelhiClimateTrain.csv` is present in this folder.

---

## How to Run

```bash
python Weather_Data_Analyzer_2.py
```

- All summary stats will print in the terminal.
- Plots will appear (see below for sample types).

---

## Output & Graphs

This script produces and displays:

1. **Annual Weather Statistics Table (console output)**

2. **Correlation Heatmap**  

3. **Line Chart:** Yearly average temperature trend

4. **Monthly Trends Plot:** Showcases temperature curves for each year

5. **Bar Graph:** Yearly wind speed distribution (proxy for rainfall)

6. **Scatter Plot:** Humidity vs. Temperature (with clear seasonal trends)

7. **Regression Forecast:**  
   Displays actual values, model’s orange trendline prediction for temperature 5 years into the future, and prints MSE/RMSE.

8. **Statistical Summary:**  
   - Key annual insights: which year was hottest/most windy
   - Measures of central tendency/dispersion for all main features

---

## Project Folder Structure

```
weather-data-analyzer/
├── weather_analyzer.py               # Final Python analysis script
├── DailyDelhiClimateTrain.csv        # Dataset
├── HUMIDITY-vs-TEMP-CORRELATION.jpg  # Plot
├── TEMP-PRED-FOR-NEXT-YEARS.jpg      # Plot
└── README.md                         # This file
```

---

## Attribution

- Dataset: [Kaggle - Daily Delhi Climate Data](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data)

---

## License

MIT License  
This repository is for educational use.  
Dataset and core code may belong to original authors (see Kaggle attribution).

---

*Questions, improvements or contributions are welcome!*
