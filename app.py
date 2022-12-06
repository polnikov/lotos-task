import numpy as np
from stl import mesh
import plotly.graph_objects as go
import pandas as pd


# Функция конвертации STL модели в Mesh3d
def stl2mesh3d(stl_mesh):
    p, q, r = stl_mesh.vectors.shape #(p, 3, 3)
    vertices, ixr = np.unique(stl_mesh.vectors.reshape(p*q, r), return_inverse=True, axis=0)
    I = np.take(ixr, [3*k for k in range(p)])
    J = np.take(ixr, [3*k+1 for k in range(p)])
    K = np.take(ixr, [3*k+2 for k in range(p)])
    return vertices, I, J, K


# Визуализация модели .STL
my_mesh = mesh.Mesh.from_file('sthe_stl_model_22606154.stl')
vertices, I, J, K = stl2mesh3d(my_mesh)
x, y, z = vertices.T
colorscale = [[0, '#555555'], [1, '#e5dee5']]
mesh3D = go.Mesh3d(
    x=x,
    y=y,
    z=z,
    i=I,
    j=J,
    k=K,
    opacity=0.7,
    flatshading=True,
    color='rgba(244,22,100,0.6)',
    colorscale=colorscale,
    intensity=z,
    name='LOTUS STHE',
    showscale=True
)
title = "Mesh3d LOTUS STHE"
layout = go.Layout(
    paper_bgcolor='rgb(1,1,1)',
    title_text=title,
    title_x=0.5,
    font_color='white',
    width=1600,
    height=800,
    scene_camera=dict(
        eye=dict(x=1.25, y=1.25, z=1)),
    scene_xaxis_visible=True,
    scene_yaxis_visible=True,
    scene_zaxis_visible=True,
    scene = dict(aspectratio = dict(
        x = 4,
        y = 1,
        z = 1
    )),
)

fig = go.Figure(data=[mesh3D], layout=layout)

df = pd.read_csv('temperature.csv')

fig.add_trace(go.Mesh3d(
    x=df.x,
    y=df.y,
    z=df.z,
    i=df.i,
    j=df.j,
    k=df.k,
    colorscale='Reds',
    opacity=1,
    intensity=df.x,
))

fig.show()
