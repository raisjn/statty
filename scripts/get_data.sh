HOST=${HOST:-remarkable}
ssh root@${HOST} "cd /home/root/.statty && bash queries.sh"
scp root@${HOST}:.statty/*.json data/
