import chart_studio.plotly as py
import chart_studio
import plotly.graph_objs as go
import pandas as pd

chart_studio.tools.set_credentials_file(username='adityabham', api_key='JYEeYU1ywR6kvjQsFqmd')
mapbox_access_token = 'pk.eyJ1IjoiYWRpdHlhYmhhbSIsImEiOiJja216NDNjbDQwYWJtMm5ubjNhaWZuaXhrIn0.M_2Ah3Rn4t9WWshrbzE7NA'

main_df = pd.read_csv('Police_Data.csv')
event_types = main_df['Time of Day'].unique()
main_df['info'] = main_df[['Narrative', 'Disposition', 'Time Reported']].agg('-'.join, axis=1)

main_data = []
for event in event_types:
    event_data = dict(
        lat=main_df.loc[main_df['Time of Day'] == event, 'Latitude'],
        lon=main_df.loc[main_df['Time of Day'] == event, 'Longitude'],
        name=event,
        hovertemplate=main_df.loc[main_df['Time of Day'] == event, 'info'],
        marker=dict(size=12),
        type='scattermapbox'
    )
    main_data.append(event_data)

layout = dict(
    height=800,
    margin=dict(t=0, b=0, l=0, r=0),
    font=dict(color='#FFFFFF', size=9),
    paper_bgcolor='#000000',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=42.34003665927184,
            lon=-71.0883348525928
        ),
        pitch=0,
        zoom=15,
        style='dark'
    )
)

annotations = [dict(
    text='Northeastern University Crime Visualization Tool',
    font=dict(color='#FFFFFF', size=14), borderpad=10,
    x=0.05, y=0.05, xref='paper', yref='paper', align='left',
    showarrow=False, bgcolor='black'
)]
layout['annotations'] = annotations

updatemenus = list([
    dict(
        buttons=list([
            dict(
                args=['mapbox.style', 'dark'],
                label='Dark',
                method='relayout'
            ),
            dict(
                args=['mapbox.style', 'satellite-streets'],
                label='Satellite with Streets',
                method='relayout'
            )
        ]),
        direction='up',
        x=0.75,
        xanchor='left',
        y=0.05,
        yanchor='bottom',
        bgcolor='#000000',
        bordercolor='#FFFFFF',
        font=dict(size=11)
    )
])

layout['updatemenus'] = updatemenus
layout['title'] = 'NEU Crime Tool'

fig = go.Figure(data=main_data, layout=layout)
fig.update_layout(showlegend=True)
fig.update_layout(height=300)
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))
url = py.plot(fig, validate=False)
