#!/bin/sh

picom --config ~/.config/picom/picom.conf -b &
volumeicon &
nm-applet &
setxkbmap -model pc105 -layout us,es -option grp:alt_space_toggle &
