import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# load the processed data
df = pd.read_csv("data/formatted_sales.csv")

# sort by date as requested
df = df.sort_values(by="date")

# initialize the dash app
app = dash.Dash(__name__)

# create the line chart
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="pink morsel sales over time"
)

# build the app layout
app.layout = html.Div(children=[
    html.H1(
        children="pink morsel sales visualizer",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# run the app locally
if __name__ == "__main__":
    app.run(debug=True)