#!/usr/bin/env bash
# Create the PrivSep empty directory if necessary
if [ ! -d /run/sshd ]; then
    mkdir /run/sshd
    chmod 0755 /run/sshd
fi

# Start the SSH daemon in the foreground
exec /usr/sbin/sshd -D 2>&1
