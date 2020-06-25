class Outcome:
    def __init__(self, name: str, odds: int) -> None:
        self.name = name
        self.odds = odds

    def __str__(self):
        return f"{self.name} ,{self.odds}"
