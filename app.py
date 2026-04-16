import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# load and sort data
df = pd.read_csv("data/formatted_sales.csv")
df = df.sort_values(by="date")

# init dash app
app = dash.Dash(__name__)

# define a clean color palette
colors = {
    "bg": "#f4f4f5",
    "text": "#27272a",
    "accent": "#e10098" # pink for pink morsels
}

# app layout with inline css styling
app.layout = html.Div(
    style={
        "backgroundColor": colors["bg"],
        "fontFamily": "sans-serif",
        "padding": "20px",
        "minHeight": "100vh"
    },
    children=[
        # header
        html.H1(
            children="pink morsel sales dashboard",
            style={
                "textAlign": "center",
                "color": colors["text"]
            }
        ),

        # radio buttons for region filtering
        html.Div(
            style={
                "textAlign": "center", 
                "marginBottom": "30px",
                "fontSize": "18px"
            },
            children=[
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": " north ", "value": "north"},
                        {"label": " east ", "value": "east"},
                        {"label": " south ", "value": "south"},
                        {"label": " west ", "value": "west"},
                        {"label": " all ", "value": "all"}
                    ],
                    value="all", # default selection
                    inline=True,
                    style={"color": colors["text"]}
                )
            ]
        ),

        # the graph (empty for now, callback fills it)
        dcc.Graph(id="sales-line-chart")
    ]
)

# listen to the radio button and update the graph
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):
    # filter data based on selection
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    # build new chart with filtered data
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"sales in region: {region}",
        color_discrete_sequence=[colors["accent"]]
    )

    # style the chart colors to match our theme
    fig.update_layout(
        plot_bgcolor=colors["bg"],
        paper_bgcolor=colors["bg"],
        font_color=colors["text"]
    )

    return fig

# run server
if __name__ == "__main__":
    app.run(debug=True)