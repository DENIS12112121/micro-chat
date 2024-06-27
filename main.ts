input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString(":)")
})
// programa
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
// metti la radio
radio.setGroup(1)
