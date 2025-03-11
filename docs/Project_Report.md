# 🌡️ Temperature Change Analysis Report (1961–2019)

## 1. Introduction
This project analyzes temperature changes over time (1961–2019) for five selected countries: **China, Japan, United States of America, Brazil, and Canada**. The goal is to identify long-term trends and short-term variations in temperature change using interactive visualizations created with **Dash** and **Plotly**. By combining line and scatter plots, the project aims to provide both macro and micro-level insights into the changes over time.

This analysis is significant because it helps reveal how different countries experience climate change, providing insights into the effectiveness of environmental policies and regional climate resilience.

---

## 2. Data Management
### 2.1 Data Source
- The data was sourced from [Kaggle](https://www.kaggle.com/datasets/sevgisarac/temperature-change) and includes recorded temperature changes from **1961 to 2019**. Kaggle is a well-known platform for data sets, and this dataset is reliable and widely used for climate analysis.

The data is structured in a tabular format, making it easy to load into a DataFrame and manipulate using Python libraries like `pandas`. The long history of the data allows for detecting long-term trends and short-term fluctuations.

### 2.2 Data Cleaning
Steps taken to clean the data:
- **Filtered for five target countries** – The data initially included many countries. To focus the analysis, five diverse countries were selected to reflect different geographical and climatic patterns. The countries were chosen based on their varying climates and industrial backgrounds to provide a balanced comparison.
- **Filtered for temperature change data only** – The dataset contained multiple measurements (e.g., precipitation, humidity), but only temperature change was relevant to the study's goal.
- **Converted year columns (e.g., `Y1961`) to integer format** – This step made it easier to plot data accurately and allowed Plotly to recognize the x-axis values properly. Integer values make it easier to apply time-based functions and sorting.
- **Melted the data into long format** – Reshaping the data allowed it to be more easily visualized and handled by Plotly’s plotting functions. The long format allows each row to represent a single data point, making it easier to map it to the graph.

### 2.3 Data Format
| Column Name           | Description                                |
|----------------------|--------------------------------------------|
| **Area**              | Name of the country                        |
| **Element**           | Type of measurement (Temperature Change)    |
| **Year**              | Year of recorded data                      |
| **Temperature Change**| Recorded temperature change (°C)           |

This format ensured that each row represented a single data point, simplifying analysis and plotting. Clean and consistent data formatting reduces the risk of mapping errors during visualization.

---

## 3. Methodology
### 3.1 Why Line Graph + Scatter Plot?
- **Line Graph** → Best suited for showing long-term trends over time. Line graphs connect data points, making it easier to spot overall trends and patterns. In this case, the line graph helps visualize whether temperature changes have increased or decreased over time.

The line graph helps to identify overall trends and patterns that may not be visible when looking at individual data points. For example, consistent increases over several decades indicate a clear warming trend.

- **Scatter Plot** → Useful for visualizing yearly variations and spotting outliers. Scatter plots display individual data points, allowing for better insight into fluctuations and the variability of data across years.

The scatter plot helps to identify short-term variations and unusual spikes or drops in temperature change. It highlights outliers that might be caused by specific weather events or data collection errors.

### 3.2 Interactive Elements
- **Hover functionality** → Displays detailed year, value, and country data. When a user hovers over a point, they can see the exact temperature change value and corresponding year, improving clarity.

This feature allows users to see precise data values, which helps when comparing different countries or detecting patterns within a short time range.

- **Legend click functionality** → Allows isolation of specific country data. By clicking on a country in the legend, the user can hide or isolate that country’s data, making it easier to focus on particular trends.

This helps users focus on a single country’s trend or compare only a few countries without interference from other lines.

---

## 4. Analysis and Insights
### 4.1 General Trends
- **Temperature change has increased over time for most countries** – The line graph shows a clear upward trend in temperature change, suggesting that global temperatures are rising steadily.

Global warming trends are consistent across most countries, with a noticeable acceleration starting in the 1980s. The data confirms patterns reported by global climate monitoring agencies.

- **The magnitude of change differs significantly between countries** – While some countries show sharp increases, others have more gradual changes. This reflects differences in geographical location and climate policies.

For example, Canada shows higher variability due to its Arctic proximity, whereas China shows a steady increase, likely driven by industrialization and urban development.

### 4.2 Country-Specific Insights
- **Canada** → Higher fluctuations and more variability in data. Canada’s temperature change data shows more erratic swings, likely due to its varied climate zones and exposure to Arctic influences.

Canada’s data suggests that northern regions may be warming faster than southern regions, consistent with global findings about Arctic warming.

- **China** → More stable increase in temperature over time. China's data reflects a steady upward trend, suggesting consistent warming possibly tied to industrialization and urbanization.

China’s consistent increase might reflect long-term changes linked to carbon emissions and the expansion of urban infrastructure.

- **United States** → Consistent upward trend with moderate fluctuations. The U.S. data shows a general rise in temperature change, with occasional spikes and drops, likely linked to climate events and policy changes.

The moderate fluctuations suggest that both natural climate cycles and human activity are influencing the pattern.

---

## 5. Limitations
- **The data only includes temperature change — not absolute temperature values** – Without absolute values, it’s harder to gauge the severity of warming in specific regions.

Having absolute values would allow for more meaningful comparisons and contextual insights into temperature changes.

- **Outliers may skew the trend lines** – Sudden spikes or drops in temperature change data may result from data collection errors or extreme weather events.

Identifying and addressing outliers would improve the reliability of trend lines.

- **No geographical or seasonal breakdowns** – The dataset does not account for regional or seasonal differences, which could provide deeper insights into climate patterns.

Seasonal data would help distinguish between long-term warming and seasonal variations.

---

## 6. Future Improvements
- **Add more countries and regions for broader analysis** – Including more countries would provide a more comprehensive view of global temperature trends.

Analyzing data from additional countries and regions would make it easier to identify global patterns and regional differences.

- **Include absolute temperature data for more context** – Pairing temperature change with absolute values would offer deeper insight into the severity of warming.

Absolute values would help quantify the impact of temperature change on ecosystems and human populations.

- **Create additional interactive controls for better data exploration** – Adding filters for specific years or regions would make the visualizations more flexible and insightful.

Adding year filters or geographical breakdowns would allow users to explore data in greater detail.

---

## 7. Conclusion
This project effectively visualizes long-term trends and yearly variations in temperature change using Dash and Plotly. The line graph reveals broad patterns, while the scatter plot highlights yearly differences and outliers. The interactive elements enhance user engagement and provide valuable insights into global temperature changes.

This analysis confirms the rising trend in global temperatures and highlights the differences in how climate change manifests across countries.

---

## 8. References
- [Kaggle Dataset](https://www.kaggle.com/datasets/sevgisarac/temperature-change)
- Plotly Documentation: [https://plotly.com](https://plotly.com)
- Dash Documentation: [https://dash.plotly.com](https://dash.plotly.com)

