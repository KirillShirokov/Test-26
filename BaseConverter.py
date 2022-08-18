class BaseConverter:

    def __init__(self, value, scale):  # scale possible values: ‘C’, ‘F’ or ‘K’

        self.value = value
        self.scale = scale

    def convert(self):
        if self.scale == 'C':
            print(self.value)
        elif self.scale == 'F':
            print(f'{(9 / 5) * self.value + 32}')
        elif self.scale == 'K':
            print(f'{self.value + 273.15}')
        else:
            print('Incorrect scale')


d = BaseConverter(32, 'K')
d.convert()
