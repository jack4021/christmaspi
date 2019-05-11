from gpiozero import DigitalOutputDevice


class StatefulPin:

    def __init__(self, pin: DigitalOutputDevice, state: bool):
        self.pin = pin
        self.state = state

    def apply(self):
        self.pin.value = self.state

    def off(self):
        self.pin.off()
