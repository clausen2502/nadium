import json

class Data:
    def __init__(self):
        self.filename = "data/highscore.json"

    def getHighscore(self) -> list:
        """Returns highscore from JSON"""
        try:
            with open(self.filename, "r") as file:
                    data = json.load(file)
                    highscore = data.get("highscore")
                    return highscore
        except FileNotFoundError:
            return []
        
    def updateHighscore(self, new_highscore: int):
        """Updates the new highscore"""
        current_highscore = str(self.getHighscore())
        current_highscore = current_highscore.replace("M", "")
        new_highscore = new_highscore.replace("M", "")
        if int(new_highscore) > int(current_highscore): 
            print(f"New highscore: {new_highscore}")
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump({"highscore": new_highscore}, file, indent=1, ensure_ascii=False)

                