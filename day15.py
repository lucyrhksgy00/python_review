import matplotlib.pyplot as plt

print("MatPlotLib")

"""
figure = plt.figure()
axes = figure.add_subplot(1,1,1)
# plt.show()

figure2 = plt.figure()
axes1 = figure2.add_subplot(121)   # 3자리 digit의 경우는 ,(Comma) 생략 가능
axes2 = figure2.add_subplot(121)
axes3 = figure2.add_subplot(339)
axes4 = figure2.add_subplot(100,100,1)
plt.show()

figure3 = plt.figure()
axes31 = figure3.add_subplot(331)
axes35 = figure3.add_subplot(335)
axes39 = figure3.add_subplot(339)
plt.show()
"""

plt.rcParams["figure.figsize"] = (15, 5)

# plot
figure = plt.figure()
axes = figure.add_subplot(1,6,1)
x = [0, 1, 2, 3, 4]
y = [4, 1, 3, 5, 2]
axes.plot(x, y, linestyle='dotted', linewidth='10')
y2 = [0, 8, 5, 3, 1]
axes.plot(x, y2, color='r', marker='o')

# 한글이 깨질 때 조치 방법(Windows)
import matplotlib as mpl
path = 'C:/Windows/Fonts/malgun.ttf'
name = mpl.font_manager.FontProperties(fname=path).get_name()
print(name)
mpl.rc('font', family=name)

# 한글이 깨질 때 조치 방법(mac)
# import matplotlib as mpl
# mpl.rcParams['axes.unicode_minus'] = False
# mpl.rcParams['font.family'] = 'AppleGothic'

axes = figure.add_subplot(1,6,2)
x = ['봄', '여름', '가을', '겨울']
y = [4, 1, 3, 5]
axes.plot(x, y)

# bar
axes = figure.add_subplot(1,6,3)
axes.bar(x,y)
plt.title('계절별 분포')
plt.xlabel('계절')
plt.ylabel('분포')

# scatter
axes = figure.add_subplot(1,6,4)
x = [range(1,7)]
y = [6, 4, 1, 2, 7, 5]
size = [50, 100, 150, 600, 250, 300]
color = ['red', 'green', 'blue', 'orange', 'aqua', 'crimson']
axes.scatter(x, y, s=size, c=color)

# pie
axes = figure.add_subplot(1,3,3)
data = [1, 2, 3, 4, 5, 6]
label = ['사과', '귤', '바나나', '수박', '참외', '사발면']

axes.pie(data, labels=label, autopct='%0.1f%%')   # 소숫점 첫째 자리까지 나오게 하고 뒤에 %를 붙임; f는 float
plt.axis('equal')
plt.legend(label, loc='center right')
plt.show()

# seaborn
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="dark")

# Simulate data from a bivariate Gaussian
n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y = rng.multivariate_normal(mean, cov, n).T

# Draw a combo histogram and scatterplot with density contours
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=x, y=y, s=5, color=".15")
sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

plt.show()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")

# Create a dataset with many short random walks
rs = np.random.RandomState(4)
pos = rs.randint(-1, 2, (20, 5)).cumsum(axis=1)
pos -= pos[:, 0, np.newaxis]
step = np.tile(range(5), 20)
walk = np.repeat(range(20), 5)
df = pd.DataFrame(np.c_[pos.flat, step, walk],
                  columns=["position", "step", "walk"])

# Initialize a grid of plots with an Axes for each walk
grid = sns.FacetGrid(df, col="walk", hue="walk", palette="tab20c",
                     col_wrap=4, height=1.5)

# Draw a horizontal line to show the starting point
grid.refline(y=0, linestyle=":")

# Draw a line plot to show the trajectory of each random walk
grid.map(plt.plot, "step", "position", marker="o")

# Adjust the tick positions and labels
grid.set(xticks=np.arange(5), yticks=[-3, 3],
         xlim=(-.5, 4.5), ylim=(-3.5, 3.5))

# Adjust the arrangement of the plots
grid.fig.tight_layout(w_pad=1)

plt.show()

# plot.ly
import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
fig.show()

# pydeck - 지도(영국 교통사고)
import pydeck as pdk

# 2014 locations of car accidents in the UK
UK_ACCIDENTS_DATA = ('https://raw.githubusercontent.com/uber-common/'
                     'deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv')

# Define a layer to display on a map
layer = pdk.Layer(
    'HexagonLayer',
    UK_ACCIDENTS_DATA,
    get_position=['lng', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1)

# Set the viewport location
view_state = pdk.ViewState(
    # longitude=-1.415,
    # latitude=52.2323,
    longitude=126.5841,
    latitude=37.3359,
    zoom=6,
    min_zoom=5,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html('demo.html')