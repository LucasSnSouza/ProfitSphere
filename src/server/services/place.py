class Place:
    
    def __init__(
        self,
        name,
    ):
        self.name = name
        self._ships = []
        self._stations = []
    
    def dict(self) -> dict:
        return {
            "name": self.name,
            "ships": [ship.dict() for ship in self._ships],
            "stations": [station.dict() for station in self._stations]
        }