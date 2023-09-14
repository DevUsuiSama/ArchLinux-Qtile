#
# Created on Wed Sep 13 2023
#
# Copyright (c) 2023 UsuiSama
#

import pytz

from libqtile import bar, widget
from libqtile.config import Screen


def create_screens():
    return [
        Screen(
            top=bar.Bar(
                [
                    widget.Sep(
                        linewidth=0,
                        padding=6
                    ),
                    widget.Image(
                        filename="~/.config/qtile/icons/icons8-arch-linux.svg",
                        scale="False"
                    ),
                    widget.Sep(
                        linewidth=0,
                        padding=6
                    ),
                    widget.CurrentLayout(
                        font="MesloLGMDZ Nerd Font Mono, Bold",
                        foreground="CE00FF"
                    ),
                    widget.Sep(
                        linewidth=0,
                        padding=6
                    ),
                    widget.GroupBox(
                        active="#ffffff",
                        rounded=False,
                        highlight_color="007D55",
                        highlight_method="line",
                        borderwidth=0
                    ),
                    widget.Sep(
                        linewidth=0,
                        padding=6
                    ),
                    # widget.Prompt(),
                    widget.WindowName(
                        foreground="#00CA8A",
                        markup=True,
                        font="MesloLGMDZ Nerd Font Mono, Bold",
                        fontsize=12,
                        max_chars=40
                    ),
                    # widget.Chord(
                    #    chords_colors={
                    #        "launch": ("#00ffff", "#ffffff"),
                    #    },
                    #    name_transform=lambda name: name.upper(),
                    # ),
                    # widget.TextBox("default config", name="default"),
                    # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                    # widget.StatusNotifier(),
                    widget.Systray(),
                    widget.Sep(
                        linewidth=0,
                        padding=6
                    ),
                    widget.TextBox(
                        text='',
                        foreground="007D55",
                        padding=0,
                        fontsize=42
                    ),
                    widget.TextBox(
                        font="MesloLGMDZ Nerd Font Mono, Bold",
                        fontsize=18,
                        text='',
                        background="007D55",
                        foreground="fff",
                        padding=7
                    ),
                    widget.Clock(
                        font="MesloLGMDZ Nerd Font Mono, Bold",
                        fontsize=14,
                        background="007D55",
                        foreground="fff",
                        format="%H:%M:%S - %d/%m/%Y",
                        #update_interval=60.0,
                        update_interval=1.0,
                        timezone=pytz.timezone(
                            "America/Argentina/Buenos_Aires")
                    ),
                    widget.TextBox(
                        text='',
                        background="007D55",
                        foreground="000",
                        padding=0,
                        fontsize=42
                    ),
                    widget.NetGraph(
                        bandwidth_type="down",
                        interface="wlo1",
                        margin_x=0,
                        margin_y=0,
                        border_color="000",
                        background="000",
                        fill_color="00b2b2",
                        frequency=1,
                        graph_color="00FFFF",
                        line_width=2,
                        sample=100,
                        type="linefill"
                    ),
                    widget.Sep(
                        linewidth=0,
                        padding=6
                    ),
                    # widget.QuickExit(),
                ],
                25,
                opacity=1,
                margin=[5, 5, 1, 5],
                background="000000",
                border_width=4,  # Draw top and bottom borders
                border_color=["003D29", "000000", "003D29",
                              "000000"]  # Borders are magenta
            ),
            wallpaper="~/Imágenes/paisaje2.jpeg",
            wallpaper_mode="fill"
        )
    ]
