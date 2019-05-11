from typing import List

from gpiozero import DigitalOutputDevice

from christmaspi.pattern_factory import every_nth
from christmaspi.routine import DurationalPattern, Routine
from christmaspi.pattern import Pattern
from christmaspi.stateful_pin import StatefulPin


def chase(list_of_pins: List[DigitalOutputDevice], n: int, time_between: float) -> Routine:
    routine = Routine()
    for i in range(0, n):
        pattern = every_nth(list_of_pins, n, i)
        routine.add(DurationalPattern(pattern, time_between))
    return routine


def wip_on(list_of_pins: List[DigitalOutputDevice], time_between: float) -> Routine:
    routine = Routine()
    temp_list = []
    for pin in list_of_pins:
        pattern = Pattern()
        temp_list.append(pin)
        for p in temp_list:
            pattern.add(StatefulPin(p, True))
        routine.add(DurationalPattern(pattern, time_between))
    return routine
