class MarsRover(object):
    coordinates:list
    size: int = 10
    _turnLeft = {
        "N": "W",
        "W": "S",
        "S": "E",
        "E": "N"
    }
    _turnRight = {v:k for k,v in _turnLeft.items()}
    _moveX = {
        "N": 0,
        "E": 1,
        "S": 0,
        "W": -1
    }
    _moveY = {
        "N": 1,
        "E": 0,
        "S": -1,
        "W": 0
    }
    
    def __init__(self) -> None:
        self.coordinates = [0, 0, "N"]

    def command(self, command: str) -> str:
        for c in command:
            if(c == "L"):
                self.coordinates[2] = self._turnLeft[str(self.coordinates[2])]
            if(c == "R"):
                self.coordinates[2] = self._turnRight[str(self.coordinates[2])]
            if(c == "M"):
                self.coordinates[0] += self._moveX[str(self.coordinates[2])]
                self.coordinates[1] += self._moveY[str(self.coordinates[2])]
                for i in range(2):
                    if self.coordinates[i]<0:
                        self.coordinates[i] += self.size
                    elif self.coordinates[i]>=self.size:
                        self.coordinates[i] -= self.size
        if(command == "X"):
            return "Error"

    def getCoordinates(self):
        return self.coordinates