#!/usr/bin/env bash

directory=~/Pictures/Wallpapers/
monitor=$(hyprctl monitors | grep Monitor | awk '{print $2}')

if [ -d "$directory" ]; then
    random_background=$(find "$directory" -type f \( -iname \*.jpg -o -iname \*.jpeg -o -iname \*.png \) | shuf -n 1)

    hyprctl hyprpaper unload all
    hyprctl hyprpaper preload "$random_background"
    hyprctl hyprpaper wallpaper "$monitor, $random_background"

fi
