from christmaspi.routine import Routine


class Program:

    def __init__(self):
        self.routines = []

    def add(self, routine: Routine):
        self.routines.append(routine)

    def run(self):
        for rb in self.routines:
            rb.start()
