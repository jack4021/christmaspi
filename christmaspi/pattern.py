from stateful_pin import StatefulPin


class Pattern:

    def __init__(self):
        self.stateful_pins = []

    def add(self, stateful_pin: StatefulPin):
        self.stateful_pins.append(stateful_pin)

    def activate(self):
        for sp in self.stateful_pins:
            sp.apply()

    def deactivate(self):
        for sp in self.stateful_pins:
            sp.off()
