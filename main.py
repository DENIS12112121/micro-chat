def on_button_pressed_a():
    radio.send_string(":)")
input.on_button_pressed(Button.A, on_button_pressed_a)
#programa
def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)
#metti la radio
radio.set_group(1)