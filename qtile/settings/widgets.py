from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=1, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text=" ? "):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=50,
        padding=6
    )


def workspaces():
    return [
        widget.GroupBox(
            **base(fg='light'),
            font='Ubuntu Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['focus'],
            inactive=colors['color4'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['urgent'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [

    *workspaces(),

    #widget.Systray(background=colors['dark'], padding=3),
    #powerline('color4', 'dark'),
    #widget.TextBox(text=" ", **base(bg='color4')),
    #powerline('urgent', 'color4'),
    icon(fg="focus", bg="color1", text= ' 󰖩 '),
    widget.Net(**base(fg='focus', bg='color1'), interface='wlan0'),
    widget.TextBox(text=" ", **base(bg='color1')),
    separator(),
    icon(fg="focus", bg="color1", text= '   '),
    widget.CPU(**base(fg='focus',bg='color1')),
    widget.TextBox(text=" ", **base(bg='color1')),
    #powerline('color2', 'color4'),
    separator(),
    widget.TextBox(text=" ", **base(bg='color1')),

    #powerline('color1', 'color2'),

    icon(fg="focus",bg="color1", fontsize=17, text=' 󰃰 '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(fg='focus',bg='color1'), format='%d/%m/%Y - %H:%M '),

    #powerline('dark', 'color1'),
    separator(),
    widget.TextBox(text=" ", **base(bg='color1')),
    widget.CurrentLayoutIcon(**base(fg='focus', bg='color1'), scale=0.7),
    widget.TextBox(text=" ", **base(bg='color1')),
    
    separator(),
    widget.QuickExit(
        **base(fg='focus', bg='color1'), 
        scale=0.7, default_text="  ", 
        countdown_format='{}',
    ),
    widget.TextBox(text=" ", **base(bg='color1')),
]

secondary_widgets = [
    *workspaces(),

    #powerline('color3', 'dark'),
    icon(bg="color1", text= ' 󰠘 '),
    widget.Memory(**base(bg='color1')),
    separator(),
    widget.TextBox(text=" ", **base(bg='color1')),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65, ),

    widget.TextBox(text=" ", **base(bg='color1')),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 2,
}
extension_defaults = widget_defaults.copy()
