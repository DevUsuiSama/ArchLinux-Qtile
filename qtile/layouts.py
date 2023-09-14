#
# Created on Wed Sep 13 2023
#
# Copyright (c) 2023 UsuiSama
#

from libqtile import layout


def create_layouts():
    # Configuración de los bordes de las ventanas
    default = {
        "border_width": 1,
        "margin": 5,
        "border_focus": "1DB2ED",
        "border_normal": "1D2330",
        "single_border_width": 0,
        "single_margin": 10,
    }

    return [
        # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2),
        # layout.Columns(**_cdefault),
        layout.Max(**default),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        layout.Bsp(**default),
        # layout.Matrix(),
        # layout.MonadTall(**_cdefault),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        layout.TreeTab(
            font="Noto Sans",
            fontsize=10,
            sections=["PRIMERO", "SEGUNDO", "TERCERO", "CUARTO"],
            section_fontsize=10,
            border_width=2,
            bg_color="000000",
            active_bg="55C5F1",
            active_fg="000",
            inactive_bg="0F8CBD",
            inactive_fg="1c1f24",
            padding_left=0,
            padding_x=0,
            padding_y=5,
            section_top=10,
            section_bottom=20,
            level_shift=8,
            vspace=3,
            panel_width=200
        ),
        # layout.VerticalTile(),
        # layout.Zoomy(),
        layout.Floating(**default),
    ]
