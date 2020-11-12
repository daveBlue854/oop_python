from dataclasses import dataclass
import dataclasses
from typing import List

from src.Game import Game
from src.Player import Player


@dataclass
class Simulator:
    player: Player
    game: Game
    playerDuration: int = 250
    playerStakeMult: int = 100
    samples: int = 50
    maximums: List[int] = dataclasses.field(default_factory=list)
    durations: List[int] = dataclasses.field(default_factory=list)
