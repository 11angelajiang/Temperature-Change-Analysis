import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from dash import Dash, html, dcc

# Load the data
file_path = '/Users/angelajiang/IntroStats/statsenv/final/temperature.csv'
data = pd.read_csv(file_path, encoding='latin1')

# Select 5 countries to focus on
target_countries = ["China", "Japan", "United States of America", "Brazil", "Canada"]

data = data[data['Area'].isin(target_countries) & (data['Element'] == 'Temperature change')]

# Melt the data to long format for time-series plotting
data_melted = data.melt(id_vars=['Area'], value_vars=[f'Y{year}' for year in range(1961, 2020)],
                        var_name='Year', value_name='Temperature Change')

# Clean up the 'Year' column
data_melted['Year'] = data_melted['Year'].str[1:].astype(int)

# Create subplots for line graph and scatter plot
fig = make_subplots(rows=2, cols=1, subplot_titles=(
    'Temperature Change Over Time (1961–2019) - Line Graph',
    'Temperature Change Over Time (1961–2019) - Scatter Plot'
))

# Add line graph
for country in target_countries:
    country_data = data_melted[data_melted['Area'] == country]
    fig.add_trace(
        go.Scatter(
            x=country_data['Year'],
            y=country_data['Temperature Change'],
            mode='lines',
            name=country
        ),
        row=1, col=1
    )

# Add scatter plot
for country in target_countries:
    country_data = data_melted[data_melted['Area'] == country]
    fig.add_trace(
        go.Scatter(
            x=country_data['Year'],
            y=country_data['Temperature Change'],
            mode='markers',
            name=country
        ),
        row=2, col=1
    )

# Improve layout
fig.update_layout(
    height=800,
    width=900,
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(size=12),
    legend=dict(
        title=dict(text='Country'),
        bordercolor='LightGrey',
        borderwidth=1
    ),
    margin=dict(l=40, r=40, t=40, b=40)
)

# Improve axis properties
fig.update_xaxes(showgrid=True, gridcolor='lightgrey', zeroline=False)
fig.update_yaxes(showgrid=True, gridcolor='lightgrey', zeroline=False)

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig),
    html.Div([
        html.H3("How to Read the Graph:"),
        html.P("- The line graph above shows long-term trends in temperature change over time from 1961 to 2019 for five selected countries."),
        html.P("- The scatter plot below shows individual data points for each year, helping to identify variation and specific outliers."),

        html.H3("How to Interact:"),
        html.P("- Hover over any point to see detailed values (country, year, temperature change)."),
        html.P("- Click on a country name in the legend to isolate that country’s data."),

        html.H3("Key Takeaways:"),
        html.P("- Temperature change tends to increase over time for most countries, but the variation differs significantly."),
        html.P("- Canada shows more fluctuation, while China has a steadier trend.")
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
