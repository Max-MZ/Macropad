from adafruit_hid.keycode import Keycode

key_maps = {
    1: {
        "Name": "Linux",
        0: ([Keycode.CONTROL, Keycode.C], "Copy"),
        1: ([Keycode.CONTROL, Keycode.V], "Paste"),
        2: ([Keycode.CONTROL, Keycode.Z], "Undo"),
        3: ([Keycode.CONTROL, Keycode.Y], "Redo"),
        4: ("", ""),
        5: ("", ""),
        6: ("", ""),
        7: ("", ""),
        8: ("", ""),
        9: ([Keycode.COMMAND, Keycode.L], "Lock"),
        10: ("", ""),
        11: ("", ""),
    },
    2: {
        "Name": "TMux",
        0: ([Keycode.CONTROL, Keycode.X], "Cut"),
        1: ([Keycode.CONTROL, Keycode.C], "Copy"),
        2: ([Keycode.CONTROL, Keycode.V], "Paste"),
        3: ([Keycode.CONTROL, Keycode.Z], "Undo"),
        4: ([Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE], "Task"),
        5: ("", ""),
        6: ("", ""),
        7: ("", ""),
        8: ("", ""),
        9: ("", ""),
        10: ("", ""),
        11: ("", ""),
    },
    3: {
        "Name": "Git",
        0: ("git status\n", "status"),
        1: ("git diff\n", "diff"),
        2: ("git pull\n", "pull"),
        3: ('git commit -m "', "commit"),
        4: ("git push\n", "push"),
        5: ("", ""),
        6: ("", ""),
        7: ("", ""),
        8: ("", ""),
        9: ("", ""),
        10: ("", ""),
        11: ("", ""),
    },
    4: {
        "Name": "Numpad",
        0: (Keycode.SEVEN, "7"),
        1: (Keycode.EIGHT, "8"),
        2: (Keycode.NINE, "9"),
        3: (Keycode.FOUR, "4"),
        4: (Keycode.FIVE, "5"),
        5: (Keycode.SIX, "6"),
        6: (Keycode.ONE, "1"),
        7: (Keycode.TWO, "2"),
        8: (Keycode.THREE, "3"),
        9: (Keycode.ZERO, "0"),
        10: (Keycode.PERIOD, "."),
        11: (Keycode.ENTER, "Enter"),
    },
    5: {
        "Name": "Alt Numpad",
        0: (Keycode.HOME, "Home"),
        1: (Keycode.UP_ARROW, "Up"),
        2: (Keycode.PAGE_UP, "PgUp"),
        3: (Keycode.LEFT_ARROW, "Left"),
        4: (Keycode.K, "K"),
        5: (Keycode.RIGHT_ARROW, "Right"),
        6: (Keycode.END, "End"),
        7: (Keycode.DOWN_ARROW, "Down"),
        8: (Keycode.PAGE_DOWN, "PgDn"),
        9: (Keycode.INSERT, "Ins"),
        10: (Keycode.DELETE, "Del"),
        11: (Keycode.ENTER, "Enter"),
    },
    6: {
        "Name": "Discord",
        0: ([Keycode.CONTROL, Keycode.SHIFT, Keycode.M],"Mute"),
        1: ([Keycode.CONTROL, Keycode.SHIFT, Keycode.D],"Deafen"),
        2: ([Keycode.CONTROL, Keycode.H], "PTT"),
        3: ("",""),
        4: ("",""),
        5: ("",""),
        6: ("",""),
        7: ("", ""),
        8: ("", ""),
        9: ("", ""),
        10: ("", ""),
        11: ("", ""),    
    }
}
