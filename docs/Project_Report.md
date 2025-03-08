# 🌡️ Temperature Change Analysis Report (1961–2019)

## 1. Introduction
This project analyzes temperature changes over time (1961–2019) for five selected countries: **China, Japan, United States of America, Brazil, and Canada**. The goal is to identify long-term trends and short-term variations in temperature change using interactive visualizations created with **Dash** and **Plotly**.

---

## 2. Data Management
### 2.1 Data Source
- The data was sourced from [Kaggle](https://www.kaggle.com/datasets/sevgisarac/temperature-change) and includes recorded temperature changes from **1961 to 2019**.

### 2.2 Data Cleaning
Steps taken to clean the data:
- Filtered for five target countries.
- Filtered for temperature change data only.
- Converted year columns (e.g., `Y1961`) to integer format.
- Melted the data into long format to facilitate plotting.

### 2.3 Data Format
| Column Name           | Description                                |
|----------------------|--------------------------------------------|
| **Area**              | Name of the country                        |
| **Element**           | Type of measurement (Temperature Change)    |
| **Year**              | Year of recorded data                      |
| **Temperature Change**| Recorded temperature change (°C)           |

---

## 3. Methodology
### 3.1 Why Line Graph + Scatter Plot?
- **Line Graph** → Best suited for showing long-term trends over time.
- **Scatter Plot** → Useful for visualizing yearly variations and spotting outliers.

### 3.2 Interactive Elements
- **Hover functionality** → Displays detailed year, value, and country data.
- **Legend click functionality** → Allows isolation of specific country data.

---

## 4. Analysis and Insights
### 4.1 General Trends
- Temperature change has increased over time for most countries.
- The magnitude of change differs significantly between countries.

### 4.2 Country-Specific Insights
- **Canada** → Higher fluctuations and more variability in data.
- **China** → More stable increase in temperature over time.
- **United States** → Consistent upward trend with moderate fluctuations.

---

## 5. Limitations
- The data only includes temperature change — not absolute temperature values.
- Outliers may skew the trend lines.
- No geographical or seasonal breakdowns.

---

## 6. Future Improvements
- Add more countries and regions for broader analysis.
- Include absolute temperature data for more context.
- Create additional interactive controls for better data exploration.

---

## 7. Conclusion
This project effectively visualizes long-term trends and yearly variations in temperature change using Dash and Plotly. The interactive elements enhance user engagement and provide valuable insights into global temperature changes.

---

## 8. References
- [Kaggle Dataset](https://www.kaggle.com/datasets/sevgisarac/temperature-change)
- Plotly Documentation: [https://plotly.com](https://plotly.com)
- Dash Documentation: [https://dash.plotly.com](https://dash.plotly.com)

