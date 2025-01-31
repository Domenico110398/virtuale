class Vehicle:
    def __init__(self, plate, type, fuel):
        self.plate = plate
        self.type = type
        self.fuel = fuel
        print("game!")

    def show_info(self):
        """method to show info"""
        print(f"Plate: {self.plate}\nType: {self.type}\nFuel: {self.fuel}")