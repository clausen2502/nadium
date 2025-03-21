import json
from classes.vehicledata import VehicleData
from classes.vehicle import Vehicle

class Data:
    def __init__(self):
        self.playerdata_file = "data/player_data.json"
        self.vehicledata_file = "data/vehicle_data.json"

    def getAllVehicles(self) -> list[Vehicle]:
        """Returns a list of all vehicles"""
        try:
            with open(self.vehicledata_file, "r", encoding="utf-8") as file:
                data = json.load(file)

                vehicles = []
                for vehicle in data.values():
                    vehicle_obj = VehicleData(
                        name = vehicle["name"],
                        image = vehicle["image"])
                    vehicle.append(vehicle_obj)
                return vehicles
        except(FileNotFoundError, json.JSONDecodeError):
            return []
            
    def getAllOwnedVehicles(self) -> list[Vehicle]:
        """Returns a list of all vehicles owned"""
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                owned_dict = data["vehicles_owned"]
                
                vehicles = []
                for vehicle in owned_dict.values():
                    vehicle_obj = VehicleData(
                        name = vehicle["name"],
                        image = vehicle["image"])
                    vehicles.append(vehicle_obj)
                return vehicles
        except(FileNotFoundError, json.JSONDecodeError):
            return []

    def getHighscore(self) -> int:
        """Returns highscore from JSON"""
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return int(data.get("highscore", 0))
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
    
    def getLastScore(self) -> int:
        """Returns last score from JSON"""
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return int(data.get("last_score", 0))
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
        
    def getNadium(self) -> int:
        """Returns total nadium from JSON"""
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return int(data.get("nadium_balance", 0))
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

    def updateHighscore(self, new_highscore: str):
        """Updates the new highscore"""
        new_highscore = int(new_highscore.replace("M", ""))
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}    
        current_highscore = data.get("highscore", 0)
        if int(new_highscore) > int(current_highscore): 
            print(f"New highscore: {new_highscore}")
            data["highscore"] = int(new_highscore)
            with open(self.playerdata_file, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=1, ensure_ascii=False)

    def updateLastScore(self, last_score: str):
        """Updates the new highscore"""
        last_score = int(last_score.replace("M", ""))
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}    
        data["last_score"] = int(last_score)
        with open(self.playerdata_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=1, ensure_ascii=False)

    def addNadiumToBalance(self, amount: int):
        """add nadium to the current balance"""
        nadium_balance = self.getNadium() + amount
        try:
                with open(self.playerdata_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
                data = {}    
        print(f"Nadium collected! New nadium balance: {nadium_balance}")
        data["nadium_balance"] = nadium_balance
        with open(self.playerdata_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=1, ensure_ascii=False)

    def getSelectedVehicleName(self) -> str:
        """Gets the selected vehicle name from the json file"""
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("currently_selected", "")
        except (FileNotFoundError, json.JSONDecodeError):
            return ""
        
    def setSelectedVehicleName(self, vehicle_name) -> None:
        """Updates the selected vehicle name"""
        try:
            with open(self.playerdata_file, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}    
        data["currently_selected"] = vehicle_name
        with open(self.playerdata_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=1, ensure_ascii=False)