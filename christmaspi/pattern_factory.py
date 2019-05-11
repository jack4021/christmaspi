from typing import List

from gpiozero import DigitalOutputDevice

from pattern import Pattern, StatefulPin


def all_on(list_of_pins: List[DigitalOutputDevice]) -> Pattern:
    pattern = Pattern()
    for pin in list_of_pins:
        pattern.add(StatefulPin(pin, True))
    return pattern


def all_off(list_of_pins: List[DigitalOutputDevice]) -> Pattern:
    pattern = Pattern()
    for pin in list_of_pins:
        pattern.add(StatefulPin(pin, False))
    return pattern


def odd_on(list_of_pins: List[DigitalOutputDevice]) -> Pattern:
    pattern = Pattern()
    for i in range(0, len(list_of_pins)):
        if i % 2 == 0:
            pattern.add(StatefulPin(list_of_pins[i], True))
    return pattern


def even_on(list_of_pins: List[DigitalOutputDevice]) -> Pattern:
    pattern = Pattern()
    for i in range(0, len(list_of_pins)):
        if i % 2 == 1:
            pattern.add(StatefulPin(list_of_pins[i], True))
    return pattern


def every_nth(list_of_pins: List[DigitalOutputDevice], n: int, offset: int) -> Pattern:
    pattern = Pattern()
    for i in range(0, len(list_of_pins)):
        if (i - offset) % n == 0:
            pattern.add(StatefulPin(list_of_pins[i], True))
    return pattern
