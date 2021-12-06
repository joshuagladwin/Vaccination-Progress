import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from get_data import get_data
from datetime import date
from dateutil.relativedelta import relativedelta
import json


def line_graph(df):

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df.index, y=df['yesterday_total_doses'], mode='lines+markers', name='Total'))
    fig.add_trace(go.Scatter(x=df.index, y=df['yesterday_1st_doses'], mode='lines+markers', name='Partial Vaccination'))
    fig.add_trace(go.Scatter(x=df.index, y=df['yesterday_2nd_doses'], mode='lines+markers', name='Full Vaccination'))
    fig.add_trace(go.Scatter(x=df.index, y=df['yesterday_booster_doses'], mode='lines+markers', name='Booster Vaccination', line=dict(color='#6F00EF')))
    fig.add_trace(go.Scatter(x=df.index, y=df['seven_d_avg_total'], mode='lines', name='7 Day Avg. Total', line=dict(color='#33397F', dash='dashdot')))
    fig.add_trace(go.Scatter(x=df.index, y=df['seven_d_avg_partial'], mode='lines', name='7 Day Avg. Partial', line=dict(color='#7F2C1F', dash='dashdot')))
    fig.add_trace(go.Scatter(x=df.index, y=df['seven_d_avg_full'], mode='lines', name='7 Day Avg. Full', line=dict(color='#007F5D', dash='dashdot')))
    fig.add_trace(go.Scatter(x=df.index, y=df['seven_d_avg_booster'], mode='lines', name='7 Day Avg. Booster', line=dict(color='#AB63FA', dash='dashdot')))


    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01),
        margin=dict(
            l=0,   # left margin
            r=0,   # right margin
            b=0,   # bottom margin
            t=25,  # top margin
        ),
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1 Month",
                         step="month",
                         stepmode="backward"),
                    dict(count=2,
                         label="2 Months",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6 Months",
                         step="month",
                         stepmode="backward"),
                    dict(step="all",
                         label='All')
                ])
            ),
            type="date"
        )
    )

    start = date.today() - relativedelta(months=2)
    end = date.today()

    initial_range = [
        start, end
    ]

    fig['layout']['xaxis'].update(range=initial_range)



    for ser in fig['data']:
        ser['text']=[d.strftime('%a %d %b') for d in df.index]
        ser['hovertemplate']='%{text}<br>%{y} doses<extra></extra>'

    pio.write_html(fig, file='graph.html', include_plotlyjs='CDN')


if __name__ == '__main__':

    df = get_data()

    line_graph(df)
