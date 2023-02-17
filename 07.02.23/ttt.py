class Time:
    def __init__(self,HOUR:int,MINUT:int,SEKUND:int) -> None:
        self.hour = HOUR
        self.minut = MINUT
        self.secund = SEKUND

    def __str__(self) -> str:
        pass

    def add(self,to_hour = 0, to_minut = 0, to_second = 0):
        pass

class Hour(Time):
        pass

class Minut(Time):
        pass

class Sekund(Time):
        pass


if __name__=="__main__":
    pass