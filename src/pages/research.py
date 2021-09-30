from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from core import app
from dash.dependencies import Input, Output, State

from src.components.page_head import page_head
from src.components.research import creat_research


# 后期可以设置为自动加载文章，目前暂时作为测试
def research_page(style):
    return html.Div(
        id='body_research', className=style,
        children=[
            page_head(style, '研究'),
            creat_research([
                {
                    'describe': [
                        [
                            {'src': 'assets/static/images/imagedataVTK_cow.jpg', 'width': 0.6},
                        ],
                        [
                            '''
                            # Dash VTK

                            Dash VTK 旨在将 VTK/vtk.js 可视化集成到 Dash 框架中。
                            
                            [VTK](https://vtk.org/) 代表*Visualization Toolkit*，是一个用 C++ 编写的流行库，它也可用 Python 编写，用于在科学和医学领域进行数据处理和可视化。通常，VTK 用于可视化来自模拟或传感器（如 LIDAR 扫描仪）的 3D 几何图形。在医学领域，VTK 用于通过体积渲染和/或切片来渲染 3D 图像（即 CT、MRI 等）。
                            
                            [Vtk.js](https://kitware.github.io/vtk-js/) 另一方面是 VTK 的一个子集，它专注于它的渲染方面，但在 JavaScript 世界中。 Vtk.js 采用与它的老大哥 VTK/C++ 相同的架构和对象分解，但使其在浏览器中使用起来很友好。
                            
                            Dash VTK 使其用户能够在服务器端使用 VTK 进行任何数据处理，并提供将可视化推送到客户端以获得更好体验的基础设施。 Dash VTK 不需要 VTK，但可以无缝利用它来查看点云、CFD 模拟或任何与 3D 网格或 3D 图像相关的内容。
                            '''
                        ],
                    ],
                    'introduction': [
                        {
                            'type': 'article',
                            'content': [
                                [
                                    {'src': 'assets/static/images/imagedataVTK.jpg', 'width': 0.3},
                                ],
                                [
                                    '''
                                    # Dash VTK

                                    Dash VTK aims to integrate VTK/vtk.js visualization into the Dash framework.
                                    
                                    [VTK](https://vtk.org/) stands for *Visualization Toolkit* and is a popular library written in C++ which is also available in Python for doing data processing and visualization in the scientific and medical fields. Typically VTK is used to visualize 3D geometries from simulations or sensors such as LIDAR scanner. For the medical world, VTK is used to render 3D images (i.e. CT, MRI, ...) by doing volume rendering and/or slicing.
                                    
                                    [Vtk.js](https://kitware.github.io/vtk-js/) on the other hand is a subset of VTK that focuses on the rendering aspect of it but in the JavaScript world. Vtk.js takes the same architecture and object decomposition as its big brother VTK/C++ but makes it friendly to use inside your browser.
                                    
                                    Dash VTK enables its users to use VTK on the server side for any data processing and provides the infrastructure to push the visualization to the client side for a better experience. Dash VTK does not require VTK but can seamlessly leverage it for looking at point clouds, a CFD simulation or anything 3D mesh or 3D images related.
                                    '''
                                ],
                            ]
                        },
                        {
                            'type': 'vtk',
                            'content': []
                        }
                    ],
                },
                {
                    'describe': [
                        [
                            {'src': 'assets/static/images/ploty_3d.gif', 'width': 0.6},
                        ],
                        [
                            '''
                            # Dash 核心组件

                            Dash 附带用于交互式用户界面的增压组件。 由 Dash 团队编写和维护的一组核心组件可在“dash-core-components”库中找到。
                            
                            对于生产 Dash 应用程序，应使用 Dash Enterprise [Design Kit](https://plotly.com/dash/design-kit) 管理 Dash 核心组件的样式和布局。
                            
                            源代码位于 [plotly/dash repo](https://github.com/plotly/dash-core-components) 中的 GitHub 上。
                            ''',
                        ],
                    ],
                    'introduction': [
                        {
                            'type': 'article',
                            'content': [
                                [
                                    {'src': 'assets/static/images/ploty_example.png', 'width': 0.3},
                                ],
                                [
                                    '''
                                    # Dash Core Components

                                    Dash ships with supercharged components for interactive user interfaces. A core set of components, written and maintained by the Dash team, is available in the `dash-core-components` library library.
                                    
                                    For production Dash apps, the Dash Core Components styling & layout should be managed with Dash Enterprise [Design Kit](https://plotly.com/dash/design-kit).
                                    
                                    The source is on GitHub in the [plotly/dash repo](https://github.com/plotly/dash-core-components).
                                    
                                    These docs are using Dash version 2.0.0.
                                    
                                    ```python
                                        import dash_core_components as dcc
                                        print(dcc.__version__)
                                    ```
                                    '''
                                ],
                            ]
                        },
                        {
                            'type': 'ploty',
                            'content': []
                        }
                    ],
                }
            ]),

        ]
    )



