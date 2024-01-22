#!/bin/sh
xrandr \
 --output eDP1 --mode 1600x900 --rate 60 --pos 0x0 --primary \
 --output DP1 --off \
 --output HDMI1 --off \
 --output HDMI2 --off \
 --output VIRTUAL1 --off &
picom --config ~/.config/picom/picom.conf -b &
volumeicon &
nm-applet &
setxkbmap -model pc105 -layout us,es -option grp:alt_space_toggle &
