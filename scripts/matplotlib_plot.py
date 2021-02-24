import matplotlib.pyplot as plt
import json
from datetime import datetime

def to_ts(arr):
    return [ datetime.fromtimestamp(int(x)) for x in arr ]

xmin = datetime.fromtimestamp(1614128763 - 3600 * 6)
xmax = datetime.fromtimestamp(1614128763)
def plot_battery(plt):
    data = None
    plt.set_xlim([xmin, xmax])
    with open("data/battery.json") as f:
        data = json.loads(f.read())

    x = []
    y = []
    for ts in data:
        values = data[ts]
        x.append(ts)
        y.append(list(map(lambda x: x['charge_now'], values)))


    plt.plot(to_ts(x), y, label='battery')


def plot_cpu(plt):
    data = None
    plt.set_xlim([xmin, xmax])
    with open("data/pidstats.json") as f:
        data = json.loads(f.read())
    x = []
    from collections import defaultdict

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
    for i, key in enumerate(keys):
        y = []
        for ts in x:
            if not ts in ys[key]:
                y.append(None)
            else:
                y.append(ys[key][ts]['%cpu'])

        plt.plot(to_ts(x), y, 'x', label=key)
        plt.legend([key])

f, axes = plt.subplots(2, 1)
plot_battery(axes[1])
plot_cpu(axes[0])
plt.show()
