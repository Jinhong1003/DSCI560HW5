import pandas as pd
import numpy as np
from bokeh.plotting import figure,show, output_notebook,ColumnDataSource,curdoc
from bokeh.io import push_notebook
from bokeh.models import HoverTool
from ipywidgets import interact
from bokeh.models import FactorRange
from bokeh.io import show
from bokeh.models import Panel, Tabs
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure
# output_notebook()
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.io import show
from bokeh.models import CustomJS, Select
from bokeh.models import Title


#Import the data
data=pd.read_csv('latimes-state-totals.csv')
data.head()
# print(data[""])
# # print(data[])
data['date_time']=pd.to_datetime(data['date'])
dataAug = data[(data["date"]>="2020-08-01")&(data["date"]<="2020-08-31")]
# Make a plot of new confirmed cases

dataAug['date_time'] = pd.to_datetime(dataAug['date'])

# Output to the notebook
output_notebook()  # use output_file if using a HTML file

# Create a new plot
tl = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
p = figure(tools=tl,
           plot_height=400,
           y_axis_label='New Confirmed Cases',
           title='new confirmed cases of Coronavirus',
           x_axis_type='datetime'
           )

r = p.line('date_time', 'new_confirmed_cases', source=dataAug)
p.circle('date_time', 'new_confirmed_cases', source=dataAug, fill_color="yellow", size=7)
# p.add_layout(Title(text='Date of last update:2020-10-14', text_font_style="italic"), 'above')
# p.add_layout(Title(text='Url:https://github.com/JoyKuan/california-coronavirus-data/blob/master/latimes-state-totals.csv', text_font_style="italic"), 'above')
p.add_layout(Title(text='Source: The aggregation of all local agency reports logged by Los Angeles Times reporters ', text_font_style="italic"), 'above')
p.add_layout(Title(text='Date of last update:2020-10-14', text_font_style="italic"), 'above')
# citation = Label(x=300, y=200, x_units='screen', y_units='screen',
#                  text='Source:Each row contains the aggregation of all local agency reports logged by Los Angeles Times reporters;\n    Date of last update:2020-10-14', render_mode='css',
#                  border_line_color='black', border_line_alpha=1.0,
#                  background_fill_color='white', background_fill_alpha=1.0)
# p.add_layout(citation)

p.add_tools(HoverTool(
    tooltips=[
        ('date', '@date_time{%Y-%m-%d}'),
        ('new cases', '@new_confirmed_cases')
    ],

    formatters={
        '@date_time': 'datetime',  # use 'datetime' formatter for '@date_time' field
    }
))

#####second
race="asian"
exact_date="2020-10-14"
data1=pd.read_csv('cdph-race-ethnicity.csv')
datafinal=data1.loc[data1['age']=="all"].loc[data1['date']==exact_date]
ccp_list=datafinal[["confirmed_cases_percent"]]
ccp_list=ccp_list["confirmed_cases_percent"].tolist()

pp_list=datafinal[["population_percent"]]
pp_list=pp_list["population_percent"].tolist()

dp_list=datafinal[["deaths_percent"]]
dp_list=datafinal["deaths_percent"].tolist()

race=["Asian","Black","cdph-other","Latino",'Other',"White"]

#fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
case=["Case_percent","Population_percent"]
#years = ['2015', '2016', '2017']

# data = {'fruits' : fruits,
#         '2015'   : [2, 1, 4, 3, 2, 4],
#         '2016'   : [5, 3, 3, 2, 4, 6],
#         '2017'   : [3, 2, 4, 4, 5, 3]}

data={'Race':race,
      "Case_percent":ccp_list,
      "Population_percent":pp_list
}

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
#x = [ (fruit, year) for fruit in fruits for year in years ]
x = [ (a, b) for a in race for b in case ]
counts = sum(zip(data["Case_percent"], data["Population_percent"]), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

p1 = figure(x_range=FactorRange(*x), plot_height=400, title="percent cases by race compared to representation in the general population")

r1= p1.vbar(x='x', top='counts', width=0.9, source=source,line_color="white", fill_color=factor_cmap('x', palette=['firebrick', 'olive'], factors=case, start=1, end=2))

p1.add_tools(HoverTool(
    tooltips=[
        ('x_axi','@x'),
        ('percentage', '@counts')
    ]
))
p1.y_range.start = 0
p1.x_range.range_padding = 0.1
p1.xaxis.major_label_orientation = 1
p1.xgrid.grid_line_color = None
p1.add_layout(Title(text='Url:https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx', text_font_style="italic"), 'above')
p1.add_layout(Title(text='Source:California Department of Public Health', text_font_style="italic"), 'above')
p1.add_layout(Title(text='Date of last update:2020-10-14', text_font_style="italic"), 'above')
# citation1 = Label(x=300, y=200, x_units='screen', y_units='screen',
#                  text='Source:California Department of Public Health   Date of last update:2020-10-14', render_mode='css',
#                  border_line_color='black', border_line_alpha=1.0,
#                  background_fill_color='white', background_fill_alpha=1.0)
# p1.add_layout(citation1)


date_list = sorted(list(set(data1['date'])), reverse=True)






######thrid
race1 = ["Asian", "Black", "cdph-other", "Latino", 'Other', "White"]

case1 = ["Death_percent", "Population_percent"]

data = {'Race': race1,
        "Death_percent": dp_list,
        "Population_percent": pp_list
        }
x1 = [(a, b) for a in race1 for b in case1]
counts1 = sum(zip(data["Death_percent"], data["Population_percent"]), ())  # like an hstack

source1 = ColumnDataSource(data=dict(x=x1, counts=counts1))

p2 = figure(x_range=FactorRange(*x1), plot_height=400,
            title="Death percent by race compared to representation in the general population")
r2 = p2.vbar(x='x', top='counts', width=0.9, source=source1, line_color="white",
             fill_color=factor_cmap('x', palette=['firebrick', 'olive'], factors=case, start=1, end=2))

p2.add_tools(HoverTool(
    tooltips=[
        ('x_axis', '@x'),
        ('percentage', '@counts')
    ]
))
p2.y_range.start = 0
p2.x_range.range_padding = 0.1
p2.xaxis.major_label_orientation = 1
p2.xgrid.grid_line_color = None
p2.add_layout(Title(text='Url:https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx', text_font_style="italic"), 'above')
p2.add_layout(Title(text='Source:California Department of Public Health', text_font_style="italic"), 'above')
p2.add_layout(Title(text='Date of last update:2020-10-14', text_font_style="italic"), 'above')

###搜索
select = Select(title="Case_date:", value=date_list[0], options=date_list)
select1 = Select(title="Death_date:", value=date_list[0], options=date_list)
def update_data(attrname, old, new):

    a = select.value
    data1 = pd.read_csv('cdph-race-ethnicity.csv')
    datafinal = data1[data1['age'] == "all"]
    new_data_fin = datafinal[datafinal['date'] ==a]
    #     print(new_data_fin)
    ccp = new_data_fin['confirmed_cases_percent']
    pp = new_data_fin['population_percent']

    counts = sum(zip(ccp, pp), ())
    r1.data_source.data['counts'] = counts
def update_data1(attrname, old, new):

    a = select1.value
    data1 = pd.read_csv('cdph-race-ethnicity.csv')
    datafinal = data1[data1['age'] == "all"]
    new_data_fin = datafinal[datafinal['date'] ==a]
    #     print(new_data_fin)
    dp = new_data_fin['deaths_percent']
    pp = new_data_fin['population_percent']

    counts1 = sum(zip(dp, pp), ())
    r2.data_source.data['counts'] = counts1
#
for w in [select]:
    w.on_change('value', update_data)
for w1 in [select1]:
    w1.on_change('value', update_data1)
# select1 = Select(title="Option:", value=date_list[0], options=date_list)

# for w1 in [select1]:
#     w1.on_change('value', update_data1)
# w.on_change('value', update_data1)



inputs = column(select)
inputs1=column(select1)
curdoc().add_root(row(p,width=800))
curdoc().add_root(row(inputs,p1,width=800))
curdoc().add_root(row(inputs1,p2,width=800))
curdoc().title = "Sliders"

# Show the figure
# show(p)
