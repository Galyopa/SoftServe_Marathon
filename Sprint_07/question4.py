class WashingMachine:
    def __init__(self):
        self.washing = Washing
        self.rinsing = Rinsing
        self.spinning = Spinning
        self.startWashing()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


class Washing:
    def wash():
        return print("Washing...")


class Rinsing:
    def rinse():
        return print("Rinsing...")


class Spinning:
    def spin():
        return print("Spinning...")


washingMachine = WashingMachine()
washingMachine.startWashing()
