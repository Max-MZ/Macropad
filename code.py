from adafruit_macropad import MacroPad

macropad = MacroPad()

last_position = 0
while True:
    key_event = macropad.keys.events.get()

    if key_event:
        if key_event.pressed:
            if key_event.key_number is 0:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 1:
                macropad.keyboard.press(macropad.Keycode.SHIFT, macropad.Keycode.B)
                macropad.keyboard.release_all()
            if key_event.key_number is 2:
                macropad.keyboard_layout.write("Hello, World!")
            if key_event.key_number is 3:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.VOLUME_DECREMENT
                )

    macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed:
        macropad.mouse.click(macropad.Mouse.RIGHT_BUTTON)

    current_position = macropad.encoder

    if macropad.encoder > last_position:
        macropad.mouse.move(x=+5)
        last_position = current_position

    if macropad.encoder < last_position:
        macropad.mouse.move(x=-5)
        last_position = current_position
