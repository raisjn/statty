HOST=${HOST:-remarkable}
rsync --rsync-path /opt/bin/rsync -avz src/ root@${HOST}:.statty/
rsync --rsync-path /opt/bin/rsync -avz sybil root@${HOST}:.statty/sybil
