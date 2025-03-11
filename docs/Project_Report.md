# 🌡️ Temperature Change Analysis Report (1961–2019)

## 1. Introduction
This project analyzes temperature changes over time (1961–2019) for five selected countries: **China, Japan, United States of America, Brazil, and Canada**. The goal is to identify long-term trends and short-term variations in temperature change using interactive visualizations created with **Dash** and **Plotly**. By combining line and scatter plots, the project aims to provide both macro and micro-level insights into the changes over time.

---

## 2. Data Management
### 2.1 Data Source
- The data was sourced from [Kaggle](https://www.kaggle.com/datasets/sevgisarac/temperature-change) and includes recorded temperature changes from **1961 to 2019**. Kaggle is a well-known platform for data sets, and this dataset is reliable and widely used for climate analysis.

### 2.2 Data Cleaning
Steps taken to clean the data:
- **Filtered for five target countries** – The data initially included many countries. To focus the analysis, five diverse countries were selected to reflect different geographical and climatic patterns.
- **Filtered for temperature change data only** – The dataset contained multiple measurements, but only temperature change was relevant to the study's goal.
- **Converted year columns (e.g., `Y1961`) to integer format** – This step made it easier to plot data accurately and allowed Plotly to recognize the x-axis values properly.
- **Melted the data into long format** – Reshaping the data allowed it to be more easily visualized and handled by Plotly’s plotting functions.

### 2.3 Data Format
| Column Name           | Description                                |
|----------------------|--------------------------------------------|
| **Area**              | Name of the country                        |
| **Element**           | Type of measurement (Temperature Change)    |
| **Year**              | Year of recorded data                      |
| **Temperature Change**| Recorded temperature change (°C)           |

This format ensured that each row represented a single data point, simplifying analysis and plotting.

---

## 3. Methodology
### 3.1 Why Line Graph + Scatter Plot?
- **Line Graph** → Best suited for showing long-term trends over time. Line graphs connect data points, making it easier to spot overall trends and patterns. In this case, the line graph helps visualize whether temperature changes have increased or decreased over time.
- **Scatter Plot** → Useful for visualizing yearly variations and spotting outliers. Scatter plots display individual data points, allowing for better insight into fluctuations and the variability of data across years.

### 3.2 Interactive Elements
- **Hover functionality** → Displays detailed year, value, and country data. When a user hovers over a point, they can see the exact temperature change value and corresponding year, improving clarity.
- **Legend click functionality** → Allows isolation of specific country data. By clicking on a country in the legend, the user can hide or isolate that country’s data, making it easier to focus on particular trends.

---

## 4. Analysis and Insights
### 4.1 General Trends
- **Temperature change has increased over time for most countries** – The line graph shows a clear upward trend in temperature change, suggesting that global temperatures are rising steadily.
- **The magnitude of change differs significantly between countries** – While some countries show sharp increases, others have more gradual changes. This reflects differences in geographical location and climate policies.

### 4.2 Country-Specific Insights
- **Canada** → Higher fluctuations and more variability in data. Canada’s temperature change data shows more erratic swings, likely due to its varied climate zones and exposure to Arctic influences.
- **China** → More stable increase in temperature over time. China's data reflects a steady upward trend, suggesting consistent warming possibly tied to industrialization and urbanization.
- **United States** → Consistent upward trend with moderate fluctuations. The U.S. data shows a general rise in temperature change, with occasional spikes and drops, likely linked to climate events and policy changes.

---

## 5. Limitations
- **The data only includes temperature change — not absolute temperature values** – Without absolute values, it’s harder to gauge the severity of warming in specific regions.
- **Outliers may skew the trend lines** – Sudden spikes or drops in temperature change data may result from data collection errors or extreme weather events.
- **No geographical or seasonal breakdowns** – The dataset does not account for regional or seasonal differences, which could provide deeper insights into climate patterns.

---

## 6. Future Improvements
- **Add more countries and regions for broader analysis** – Including more countries would provide a more comprehensive view of global temperature trends.
- **Include absolute temperature data for more context** – Pairing temperature change with absolute values would offer deeper insight into the severity of warming.
- **Create additional interactive controls for better data exploration** – Adding filters for specific years or regions would make the visualizations more flexible and insightful.

---

## 7. Conclusion
This project effectively visualizes long-term trends and yearly variations in temperature change using Dash and Plotly. The line graph reveals broad patterns, while the scatter plot highlights yearly differences and outliers. The interactive elements enhance user engagement and provide valuable insights into global temperature changes.

---

## 8. References
- [Kaggle Dataset](https://www.kaggle.com/datasets/sevgisarac/temperature-change)
- Plotly Documentation: [https://plotly.com](https://plotly.com)
- Dash Documentation: [https://dash.plotly.com](https://dash.plotly.com)

