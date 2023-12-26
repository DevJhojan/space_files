#!/bin/sh

# systray battery icon
cbatticon -u 2:w&

# systray volume
volumeicon &

#transparencia
#picom -b&
picom -b &
picom -config ~/.config/picom/picom.conf & 
#configuraciòn 2 pantallas
bash /home/devdragon/.screenlayout/screem.sh

#Fondo de pantalla
nitrogen --restore &

#Themer
lxappearance --restore &

## Teclado en latino
setxkbmap latam &

