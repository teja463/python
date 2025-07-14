class Microwave:
    def __init__(self, brand, power_rating):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def turn_on(self):
        if self.turned_on:
            print(f'Microwave {self.brand} already turned on')
        else:
            self.turned_on = True
            print(f'Microwave {self.brand} is now turned on')

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave {self.brand} is now turned off')
        else:
            print(f'Microwave {self.brand} is now turned off')

    def run(self, seconds):
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds')
        else:
            print('Turn on the microwave first')

    def __str__(self):
        return f'{self.brand} of rating {self.power_rating})'

    def __repr__(self):
        return f'Microwave(brand="{self.brand}" rating="{self.power_rating}")'


smeg: Microwave = Microwave('Smeg', 'B')

print(smeg)
print(repr(smeg))

smeg.turn_on()
smeg.run(19)
smeg.turn_off()
