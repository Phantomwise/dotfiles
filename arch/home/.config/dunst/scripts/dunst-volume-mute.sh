#!/bin/bash

# Check volume status using wpctl
volume_status=$(wpctl get-volume @DEFAULT_AUDIO_SINK@)

# Parse the output to check if muted
if echo "$volume_status" | grep -q "[MUTED]"; then
    dunstify "Volume Muted" -u normal -r 118111108 -i volume-mute
else
    dunstify "Volume Unmuted" -u normal -r 118111108 -i volume-unmute
fi