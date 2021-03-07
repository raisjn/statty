from bokeh.layouts import gridplot
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.palettes import d3

import json
import time
from datetime import datetime

def to_ts(arr):
    return [ datetime.fromtimestamp(int(x)) for x in arr ]

# plot the last week of data
# TODO: make configurable
xmin = datetime.fromtimestamp(time.time() - 3600 * 24 * 7)
xmax = datetime.now()

TOOLTIPS = [
    ("time", "@time"),
    ("value", "$y"),
    ("label", "@label"),
]

def plot_battery(plt):
    data = None
    # plt.set_xlim([xmin, xmax])
    with open("data/battery.json") as f:
        data = json.loads(f.read())

    plt.y_range.start = 0
    plt.x_range.start = xmin
    plt.x_range.end = xmax
    x = []
    y = []
    for ts in data:
        values = data[ts]
        x.append(ts)
        y.append(list(map(lambda x: x['charge_now'] / x['charge_full'], values)))


    plt.line(to_ts(x), y)


def plot_cpu(plt):
    data = None
    # plt.set_xlim([xmin, xmax])
    with open("data/pidstats.json") as f:
        data = json.loads(f.read())
    x = []
    from collections import defaultdict
    plt.x_range.start = xmin
    plt.x_range.end = xmax

    ys = defaultdict(dict)
    for ts in data:
        values = data[ts]
        x.append(ts)

        for obj in values:
            key = obj['command']
            ys[key][ts] = obj

    keys = list(ys.keys())
    keys.sort()


    x.sort(key=lambda x: int(x))
    palette = d3['Category20'][20]
    for i, key in enumerate(keys):
        y = []
        for ts in x:
            if not ts in ys[key]:
                y.append(None)
            else:
                y.append(ys[key][ts]['%cpu'])

        cd = ColumnDataSource(data=dict(
            x=to_ts(x),
            y=y,
            label=[key]*len(y),
            time=x
        ))
        color = palette[i % len(palette)]
        plt.scatter('x', 'y', color=color, source=cd)

p1 = figure(x_axis_type="datetime", title="Battery", tooltips=TOOLTIPS)
p2 = figure(x_axis_type="datetime", title="CPU Usage", tooltips=TOOLTIPS)
plot_battery(p1)
plot_cpu(p2)

show(gridplot([[p1],[p2]], plot_width=1200, plot_height=400))  # open a browser
