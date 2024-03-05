class MarsRover(object):
    coordinates = [0, 0, "N"]
    _turnLeft = {
        "N": "W",
        "W": "S",
        "S": "E",
        "E": "N"
    }
    # Pour plus tard
    _turnRight = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }
    
    def __init__(self) -> None:
        self.coordinates = [0, 0, "N"]

    def command(self, command: str) -> str | None:
        for c in command:
            if(c == "L"):
                self.coordinates[2] = self._turnLeft[str(self.coordinates[2])]
            if(c == "R"):
                self.coordinates[2] = self._turnRight[str(self.coordinates[2])]
        if(command == "X"):
            return "Error"

    def getCoordinates(self):
        return self.coordinates