class ComplexOutcome:
    """
    this class is the same as the Outcome class above
    but here i didn't use the dataclass decorator,
    just did all the implementation by hand
    """

    def __init__(self, name: str, odds: int) -> None:
        self.name = name
        self.odds = odds

    def __str__(self):
        return f"{self.name}, {self.odds}"

    def __repr__(self):
        return f"{self.__class__.__name__:s} : name={self.name!r}, odds={self.odds!r}"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def winAmount(self, amount: int):
        return self.odds * amount
