
## installation

### on PC:

`bash sync.sh` to sync files to ~/.statty/ on rM

### on rM:

* `opkg install python3`
* `opkg install sysstat`
* `cd ~/.statty/ && bash install.sh`

then run `collect_stats.sh` by hand to verify it works:

* `cd ~/.statty/ && bash collect_stats.sh`

if it works, turn on the system collector service:

* `systemctl enable statty --now`


## looking at data

* from base dir, run `bash ./scripts/get_data.sh` to retrieve data from rM
* to visualize, run `python ./scripts/plot_bokeh.py`

