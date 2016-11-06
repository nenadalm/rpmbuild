#!/usr/bin/env bash

set -eu

function autostart() { 
    while true; do
        if pidof awesome; then
            break
        fi
        sleep 1
    done

    dex-autostart -a -e Awesome
}

eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK
autostart &

exec awesome --no-argb

