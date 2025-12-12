import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, dcc, Input, Output


# CARGA DE DATOS

df_prophet = pd.read_csv("product/predicciones_prophet.csv")
df_sarima = pd.read_csv("product/predicciones_sarima.csv")
df_hist = pd.read_csv("data/agg_day.csv")

df_hist['fecha'] = pd.to_datetime(df_hist['fecha'])
df_prophet['ds'] = pd.to_datetime(df_prophet['ds'])
df_sarima['ds'] = pd.to_datetime(df_sarima['ds'])

entidades = sorted(df_hist['entidad'].unique())



# DASHBOARD

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Dashboard de Predicción de Errores por Entidad", style={'textAlign':'center'}),

    html.Br(),

    # Selector de entidad
    html.Div([
        html.Label("Seleccione una entidad:", style={'fontWeight':'bold'}),
        dcc.Dropdown(
            id='selector_entidad',
            options=[{"label": str(e), "value": e} for e in entidades],
            value=entidades[0],
            clearable=False
        )
    ], style={'width': '40%', 'margin': 'auto'}),

    html.Br(),

    # Gráfica principal
    dcc.Graph(id='grafico_predicciones'),

    html.Br(),

    # Tabla resumen
    html.H3("Tabla de predicciones (próximos 7 días)", style={'textAlign':'center'}),
    dcc.Graph(id='tabla_predicciones'),

    html.Br(),

    # Heatmap semanal
    html.H3("Mapa de calor semanal de errores históricos", style={'textAlign':'center'}),
    dcc.Graph(id='heatmap_semanal'),

], style={'padding':'30px'})



# GRÁFICAS DINÁMICAS


@app.callback(
    Output('grafico_predicciones', 'figure'),
    Output('tabla_predicciones', 'figure'),
    Output('heatmap_semanal', 'figure'),
    Input('selector_entidad', 'value')
)
def actualizar_dashboard(entidad):

    # Filtrar datos
    hist = df_hist[df_hist['entidad'] == entidad]
    prop = df_prophet[df_prophet['entidad'] == entidad]
    sar = df_sarima[df_sarima['entidad'] == entidad]

    
    # Gráfica principal
    
    fig = go.Figure()

    # Observado
    fig.add_trace(go.Scatter(
        x=hist['fecha'], y=hist['errores'],
        mode='lines+markers',
        name='Datos observados',
        line=dict(color='black')
    ))

    # Prophet
    fig.add_trace(go.Scatter(
        x=prop['ds'], y=prop['yhat'],
        mode='lines',
        name='Prophet',
        line=dict(color='blue')
    ))

    # Banda Prophet
    fig.add_trace(go.Scatter(
        x=prop['ds'], y=prop['yhat_upper'],
        line=dict(width=0),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=prop['ds'], y=prop['yhat_lower'],
        fill='tonexty',
        fillcolor='rgba(0,0,255,0.2)',
        line=dict(width=0),
        name='Rango Prophet'
    ))

    # SARIMA
    fig.add_trace(go.Scatter(
        x=sar['ds'], y=sar['sarima_pred'],
        mode='lines',
        name='SARIMA',
        line=dict(color='red')
    ))

    # Banda SARIMA
    fig.add_trace(go.Scatter(
        x=sar['ds'], y=sar['sarima_upper'],
        line=dict(width=0),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=sar['ds'], y=sar['sarima_lower'],
        fill='tonexty',
        fillcolor='rgba(255,0,0,0.2)',
        line=dict(width=0),
        name='Rango SARIMA'
    ))

    fig.update_layout(
        title=f"Predicción de errores para la entidad {entidad}",
        xaxis_title="Fecha",
        yaxis_title="Errores",
        template='plotly_white'
    )


 

# Tabla resumen (próximos 7 días)

# Filtrar predicciones futuras (mayores a la fecha máxima del histórico)
    futuros = prop[prop['ds'] > hist['fecha'].max()]

    # Tomar los próximos 7 días
    tabla = futuros[['ds','yhat','yhat_lower','yhat_upper']].head(7)

    fig_tabla = go.Figure(data=[go.Table(
        header=dict(values=list(tabla.columns),
                    fill_color='lightgray',
                    align='left'),
        cells=dict(values=[tabla[c] for c in tabla.columns]))])


    # Heatmap semanal
  
    hist['dia_semana'] = hist['fecha'].dt.day_name()
    hist['semana_del_anio'] = hist['fecha'].dt.isocalendar().week

    pivot = hist.pivot_table(
        index='dia_semana',
        columns='semana_del_anio',
        values='errores',
        aggfunc='mean'
    )

    heat = px.imshow(
        pivot,
        color_continuous_scale='Reds',
        aspect='auto',
        labels=dict(color='Errores'),
        title=f"Heatmap semanal de errores - Entidad {entidad}"
    )


    return fig, fig_tabla, heat



# EJECUTAR SERVIDOR

if __name__ == "__main__":
    app.run(debug=True, port=8060)
