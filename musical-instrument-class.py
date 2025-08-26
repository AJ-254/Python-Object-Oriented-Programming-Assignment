# Assignment 1: Musical Instrument Class
class MusicalInstrument:
    def __init__(self, name, instrument_type, brand):
        self.name = name
        self.instrument_type = instrument_type
        self.__brand = brand   # encapsulation: private attribute

    def play(self):
        return f"{self.name} is making music "

    def tune(self):
        return f"Tuning the {self.name}..."

    # Getter method for encapsulated brand
    def get_brand(self):
        return f"Brand: {self.__brand}"

# Inheritance layer
class Guitar(MusicalInstrument):
    def __init__(self, name, brand, number_of_strings):
        super().__init__(name, "String", brand)
        self.number_of_strings = number_of_strings

    def play(self):  # polymorphism: overriding play()
        return f"Strumming the {self.number_of_strings}-string {self.name} "

class Piano(MusicalInstrument):
    def __init__(self, name, brand, keys):
        super().__init__(name, "Keyboard", brand)
        self.keys = keys

    def play(self):  # polymorphism: overriding play()
        return f"Playing a melody on the {self.keys}-key {self.name} "


# Example of objects
guitar1 = Guitar("Acoustic Guitar", "Yamaha", 6)
piano1 = Piano("Grand Piano", "Steinway", 88)

print(guitar1.tune())
print(guitar1.play())
print(guitar1.get_brand())
print(piano1.tune())
print(piano1.play())
print(piano1.get_brand())
