# icmp-ttl-spoofer
A script for spoof the system TTL.


## Disabling icmp 
*For Linux:*

> echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all

*For Windows (Fw level):*

> netsh advfirewall firewall add rule name="Block system ICMP" protocol=icmpv4:8,any dir=in action=block
Allow the script in the firewall.

##  Set script as a system service
*For Linux:*

    cd /etc
    git clone https://github.com/kheabrosec/icmp-ttl-spoofer.git

    vi /lib/systemd/system/icmp-ttl-spoofer.service
    paste this:

> [Unit]
Description=Ping spoofer
After=multi-user.target
[Service]
Restart=on-failure
RestartSec=5s
Type=idle
ExecStart=/etc/ping-ttl-spoofer/ping_ttl_spoofer.py 127 (Change the ttl)
WorkingDirectory=/etc/ping_ttl_spoofer
[Install]
WantedBy=multi-user.target

    systemctl daemon-reload
    systemctl enable ping-ttl-spoofer
    systemctl start ping-ttl-spoofer

