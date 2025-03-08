import json

class Data:
    def __init__(self):
        self.filename = "data/highscore.json"

    def getHighscore(self) -> int:
        """Returns highscore from JSON"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return int(data.get("highscore", 0))
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

    def getNadium(self) -> int:
        """Returns total nadium from JSON"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return int(data.get("nadium_balance", 0))
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

    def updateHighscore(self, new_highscore: str):
        """Updates the new highscore"""
        new_highscore = int(new_highscore.replace("M", ""))
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}    
        print(f"New highscore: {new_highscore}")
        current_highscore = data.get("highscore", 0)
        if int(new_highscore) > int(current_highscore): 
            data["highscore"] = int(new_highscore)
            with open(self.filename, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=1, ensure_ascii=False)

    def addNadiumToBalance(self, amount: int):
        """add nadium to the current balance"""
        nadium_balance = self.getNadium() + amount
        try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
                data = {}    
        print(f"New nadium balance: {nadium_balance}")
        data["nadium_balance"] = nadium_balance
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=1, ensure_ascii=False)