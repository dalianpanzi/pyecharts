# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:01:55 2024

@author: chen
"""
import os
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType,SymbolType

geo=Geo(init_opts=opts.InitOpts(width='1200px',height='900px'))
geo.add_schema(maptype="world")#itemstyle_opts=opts.ItemStyleOpts 地图颜色、多边形样式...

#添加未知坐标点
new_coor="XXX.json"
geo.add_coordinate_json(new_coor)
#geo.add_coordinate('Oman',55.98,21.47) 单独加

attr=["Singapore", "Oman","Indonesia", "Philippines","Korea","India","Qatar", "United Arab Emirates","Maldives",
 "Malaysia","Taiwan", "Pakistan", "Spain", "United Kingdom", "Russia", "Netherlands","New Zealand", "Australia",
 "Panama", "Ecuador","Mexico","Peru", "Nicaragua", "Brazil", "Egypt", "Mauritania"]
value=[6,4,4,6,1,2,1,1,1,13,4,1,2,1,2,1,1,2,1,4,2,1,1,2,2,2]

geo.add("工程数量",[list(z) for z in zip(attr,value)],type_=ChartType.EFFECT_SCATTER)
#type_有 scatter、effectScatter、Heatmap、lines
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=15), title_opts=opts.TitleOpts(title="2017-2022年工程位置分布")) #max_:color_bar最大值
geo.render("XXX.html")#会放在project下

os.system("see.html")#打开html

#一页多图
def Geo_effectscatter() :
    c = (
    Geo()
    .add_schema(maptype="china")
    .add(
        "geo",
        [list(z) for z in zip(['广东', '北京', '上海', '江西', '湖南', '浙江', '江苏'],[99, 132, 47, 44, 45, 122, 107])],
        type_=ChartType.EFFECT_SCATTER,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Geo-EffectScatter"))
    )
    return c

def Geo_HeatMap() :
    c = (
    Geo()
    .add_schema(maptype="china")
    .add(
        "geo",
        [list(z) for z in zip(['广东', '北京', '上海', '江西', '湖南', '浙江', '江苏'],[99, 132, 47, 44, 45, 122, 107])],
        type_=ChartType.HEATMAP,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo_HeatMap"),
    )
    )
    return c

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        Geo_effectscatter(),
        Geo_HeatMap(),
    )
    page.render("page_draggable_layout.html")

if __name__ == "__main__":
    page_draggable_layout()
