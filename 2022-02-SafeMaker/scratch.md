
    yum install squid
    systemctl enable squid
    systemctl start squid
    vi /etc/squid/squid.conf
    systemctl restart squid
    less /var/log/squid/access.log

    acl http dstdomain "/etc/squid/allowed.txt"  # whitelisted domains