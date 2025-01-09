#!/usr/bin/env python3
from nicegui import app, ui
import pyecharts.options as opts
from pyecharts.charts import Line

#x_data = []
#y_data_flow_amount = []
# Line().add_xaxis(xaxis_data=x_data).add_yaxis(
#     series_name="Some",
#     y_axis=y_data_flow_amount,
#     areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
#     linestyle_opts=opts.LineStyleOpts(),
#     label_opts=opts.LabelOpts(is_show=False),
# ).add_yaxis(
#     series_name="Tair",
#     y_axis=y_data_rain_fall_amount,
#     yaxis_index=1,
#     areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
#     linestyle_opts=opts.LineStyleOpts(),
#     label_opts=opts.LabelOpts(is_show=False),
# ).extend_axis(
#     yaxis=opts.AxisOpts(
#         name="Precip(mm)",
#         name_location="start",
#         type_="value",
#         max_=5,
#         is_inverse=True,
#         axistick_opts=opts.AxisTickOpts(is_show=True),
#         splitline_opts=opts.SplitLineOpts(is_show=True),
#     )
# ).set_global_opts(
#     title_opts=opts.TitleOpts(
#         title="LineChart",
#         subtitle="With zoom",
#         pos_left="center",
#         pos_top="top",
#     ),
#     tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
#     legend_opts=opts.LegendOpts(pos_left="left"),
#     datazoom_opts=[
#         opts.DataZoomOpts(range_start=0, range_end=100),
#         opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
#     ],
#     xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
#     yaxis_opts=opts.AxisOpts(name="Some speed(m^3/s)", type_="value", max_=500),
# ).set_series_opts(
#     markarea_opts=opts.MarkAreaOpts(
#         is_silent=False,
#         data=[
#             opts.MarkAreaItem(
#                 name="Some name",
#                 x=("2009/9/12-7:00", "2009/9/22-7:00"),
#                 label_opts=opts.LabelOpts(is_show=False),
#                 itemstyle_opts=opts.ItemStyleOpts(color="#DCA3A2", opacity=0.5),
#             ),
#             opts.MarkAreaItem(
#                 name="降雨量",
#                 x=("2009/9/10-7:00", "2009/9/20-7:00"),
#                 label_opts=opts.LabelOpts(is_show=False),
#                 itemstyle_opts=opts.ItemStyleOpts(color="#A1A9AF", opacity=0.5),
#             ),
#         ],
#     ),
#     axisline_opts=opts.AxisLineOpts(),
# ).render("rainfall.html")



with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs() as tabs:
        ui.tab('A')
        ui.tab('B')
        ui.tab('C')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.label('Content of A')
    with ui.tab_panel('B'):
        ui.label('Content of B')
    with ui.tab_panel('C'):
        ui.label('Content of C')


ui.run(title="TEST", 
       port=8083, 
       show=True, 
       reload=True,
       root_path="/processing",
       storage_secret="warroom123warroom")
