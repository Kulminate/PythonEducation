class Distance:

    def __init__(self, value: float, value_name: str):

        self.value = value
        if value_name == 'meters':
            self.value_name = value_name
        elif value_name == 'kilometers':
            self.value_name = value_name
        else:
            raise ValueError('value name must be meters or kilometers')


    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def value_name(self):
        return self._value_name

    @value_name.setter
    def value_name(self, value_name):
        self._value_name = value_name

    def __add__(self, other):
        if self._value_name == other._value_name:
            return Distance(self._value + other._value, self._value_name)
        elif self._value_name == "kilometers" and other._value_name == 'meters':
            return Distance(self._value + (float(other._value / 1000)), self._value_name)
        elif self._value_name == "meters" and other._value_name == 'kilometers':
            return Distance((float(self._value * 1000)) + other._value, self._value_name)

    def __str__(self):
        return f'{self._value} {self._value_name}'