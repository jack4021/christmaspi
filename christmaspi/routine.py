from time import sleep

from durational_pattern import DurationalPattern


class Routine:

    def __init__(self):
        self.durational_patterns = []

    def add(self, durational_pattern: DurationalPattern):
        self.durational_patterns.append(durational_pattern)

    def start(self):
        for dp in self.durational_patterns:
            dp.pattern.activate()
            sleep(dp.duration)
            dp.pattern.deactivate()
