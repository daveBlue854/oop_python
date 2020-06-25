class Outcome:
    def __init__(self, name: str, odds: int) -> None:
        self.name = name
        self.odds = odds

    def __str__(self):
        return f"{self.name}, {self.odds}"

    def __repr__(self):
        return f"{self.__class__.__name__:s} : name={self.name!r}, odds={self.odds!r}"
