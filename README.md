🌡️ Temperature Change Analysis (1961–2019)

📌 Description
This project analyzes temperature changes over time (1961–2019) for five selected countries using **Dash** and **Plotly**. It includes interactive visualizations (line graph + scatter plot) to explore long-term trends and yearly variations.

🚀 Installation
1. Clone the Repository
```bash
git clone https://github.com/yourusername/temperature-change-analysis.git
cd temperature-change-analysis
```

2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate   # MacOS/Linux
venv\Scripts\activate     # Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

 📊 Usage
Run the Dash App:
```bash
python src/app.py
```
- Open your browser and go to: [http://127.0.0.1:8050](http://127.0.0.1:8050)

How to Interact:
- **Hover** over any point to see detailed values (country, year, temperature change).  
- **Click** on a country name in the legend to isolate that country’s data.

 📈 Data Source
The data comes from [https://www.kaggle.com/datasets/sevgisarac/temperature-change]. It includes recorded temperature changes from 1961 to 2019 for various countries.

💡 Insights
- Temperature change tends to increase over time for most countries, but variation differs significantly.  
- **Canada** shows more fluctuation, while **China** has a steadier trend.  


📄 License
This project is licensed under the MIT License.

