from __future__ import print_function

import time
import json
import os


RM1_POWER_PATH = "/sys/class/power_supply/max77818_battery/"
RM2_POWER_PATH = "/sys/class/power_supply/bq27441-0/"
def process_battery_stats():
    if os.path.exists(RM1_POWER_PATH):
        read_battery_stats(RM1_POWER_PATH)

    if os.path.exists(RM2_POWER_PATH):
        read_battery_stats(RM2_POWER_PATH)


    # read_battery_stats("/sys/class/power_supply/BAT0")


def read_battery_stats(dir):
    obj = {}

    def update_value(nm, default=-1):
        fname = os.path.join(dir, nm)
        with open(fname) as f:
            data = f.read()
            obj[nm] = int(data)
            return

        obj[nm] = default

    update_value("current_now")
    update_value("charge_now")
    update_value("charge_full")
    update_value("charge_full_design")

    obj["charge_mct"] = int(obj["charge_now"] / float(obj["charge_full"]) * 10000)
    obj["time"] = int(time.time())

    print(json.dumps(obj))

if __name__ == "__main__":
    process_battery_stats()
