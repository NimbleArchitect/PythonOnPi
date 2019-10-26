#!/bin/bash

echo "allowing network to activate"
sleep 10m

while true; do
        echo "checking network status"
        curl --silent http://example.com/index.html > /dev/null;
        if [[ $? == 0 ]]; then
                sleep 5m
        else
                echo "network lost, restarting!
                reboot
        fi
done
