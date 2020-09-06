class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheelr(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.obj.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return self.obj.__dict__[attr]

    def original_dict(self):
        return print(self.__dict__)


motorCycle = MotorCycle()
obj_mc = Adapter(motorCycle, wheels=motorCycle.TwoWheeler)
print("A {0} is a {1} vehicle".format(obj_mc.name, obj_mc.wheels()))

truck = Truck()
obj_tr = Adapter(truck, wheels=truck.EightWheeler)
print("A {0} is a {1} vehicle".format(obj_tr.name, obj_tr.wheels()))
