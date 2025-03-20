
class VehicleData:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def __repr__(self):
        return f"VehicleData(name='{self.name}', image='{self.image}')"