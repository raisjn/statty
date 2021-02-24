# TODO: verify this is right
echo statty requires 'sysstat' and 'python3' from opkg
cp statty.service /lib/systemd/system/
echo copied statty.service into /lib/systemd/system
cp statty /opt/bin/
echo copied statty into /opt/bin
chmod +x /opt/bin/statty
echo run 'systemctl enable statty --now' to turn on statty
