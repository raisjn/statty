# collection period in seconds
INTERVAL=${INTERVAL:-60}

# FLAGS FOR PIDSTAT
# -u collects cpu stats
# -r collects mem stats
# -l add the command arguments
FLAGS="-u -r -l -H"

DB_DIR="./db"
SYBIL_FLAGS="-table perf@pidstats -dir ${DB_DIR}"
BATTERY_FLAGS="-table perf@battery -dir ${DB_DIR}"

LAST_DIGEST=$(date +%s)
SYBIL_BIN=./sybil

iter=0
while [[ 1 ]]; do
  python3 battery_stats.py | ${SYBIL_BIN} ingest ${BATTERY_FLAGS}

  pidstat ${FLAGS} -h ${INTERVAL} 1 | python3 parse_stats.py ${INTERVAL} | ${SYBIL_BIN} ingest ${SYBIL_FLAGS}
  ex=$?
  if [ $ex -ne 0 ]; then
    break
  fi


  now=$(date +%s)
  mod_iter=$(($now - $LAST_DIGEST))
  if [ $mod_iter -gt 3600 ]; then
    echo "DIGEST ITER $iter, SINCE LAST DIGEST", $mod_iter
    ${SYBIL_BIN} digest ${SYBIL_FLAGS} 2>/dev/null &
    LAST_DIGEST=$now
  fi


  iter=$((iter+1))
done
