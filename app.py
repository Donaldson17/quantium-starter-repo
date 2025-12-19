#!/usr/bin/env python3
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

DATA_PATH = "data/processed/pink_morsels_sales.csv"

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    daily = df.groupby('Date', as_index=False)['Sales'].sum()
    daily = daily.sort_values('Date')
    return daily

def make_figure(df):
    fig = px.line(df, x='Date', y='Sales', title='Pink Morsels — Daily Sales',
                  labels={'Date':'Date', 'Sales':'Sales'})
    
    # add vertical marker for the price increase date
    # use a native Python datetime to avoid pandas Timestamp arithmetic inside plotly
    vdate = pd.to_datetime('2021-01-15').to_pydatetime()
    
    # add a vertical line as a shape (avoids plotly's internal averaging bug)
    fig.add_shape(type='line', x0=vdate, x1=vdate, y0=0, y1=1,
                  xref='x', yref='paper', line=dict(color='red', dash='dash'))
    fig.add_annotation(x=vdate, y=1, yref='paper', showarrow=False,
                       text='Price increase 2021-01-15', xanchor='left', yanchor='bottom')
    fig.update_layout(hovermode='x unified')
    return fig

app = Dash(__name__)

df = load_data()
fig = make_figure(df)

app.layout = html.Div(children=[
    html.H1("Pink Morsels Sales Visualiser"),
    html.P("Were sales higher before or after the price increase on 2021-01-15?"),
    dcc.Graph(id='sales-line', figure=fig)
],
    style={'width':'90%','maxWidth':'1000px','margin':'auto','fontFamily':'Arial'})

if __name__ == '__main__':
    app.run(debug=True)
