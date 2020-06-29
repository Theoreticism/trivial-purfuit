class Player(object):
    def __init__(self, name):
        self.name = name

class Protective(object):
    """protected property demo"""
    #
    def __init__(self, start_protected_value=0):
        self.protected_value = start_protected_value
    #
    @property
    def protected_value(self):
        return self._protected_value
    #
    @protected_value.setter
    def protected_value(self, value):
        if value != int(value):
            raise TypeError("protected_value must be an integer")
        if 0 <= value <= 100:
            self._protected_value = int(value)
        else:
            raise ValueError("protected_value must be " +
                             "between 0 and 100 inclusive")
    #
    @protected_value.deleter
    def protected_value(self):
        raise AttributeError("do not delete, protected_value can be set to 0")