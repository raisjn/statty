./sybil query -table perf@battery --time-bucket 60 --read-log --time -int charge_now,charge_full -int-filter charge_now:gt:0 --json > battery.json
./sybil query -table perf@pidstats --time-bucket 60 --read-log --time --group command -int "%cpu","%mem" --json > pidstats.json

