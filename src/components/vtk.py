from dash import html
# 此包需要下载
import dash_vtk
from dash_vtk.utils import to_volume_state

from vtkmodules.vtkImagingCore import vtkRTAnalyticSource

# Use VTK to get some data
data_source = vtkRTAnalyticSource()
data_source.Update()  # <= Execute source to produce an output
dataset = data_source.GetOutput()

# Use helper to get a volume structure that can be passed as-is to a Volume
volume_state = to_volume_state(dataset)  # No need to select field

content = dash_vtk.View([
    dash_vtk.VolumeRepresentation([
        # GUI to control Volume Rendering
        # + Setup good default at startup
        dash_vtk.VolumeController(size=(300, 200)),
        # Actual volume
        dash_vtk.Volume(state=volume_state),
    ]),
])


def creat_vtk(vtk_content):
    return html.Div(
        style={"width": "100%", "height": "600px"},
        children=[content],
    )

