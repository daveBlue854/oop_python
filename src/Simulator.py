from dataclasses import dataclass
from typing import List

from src.Game import Game
from src.Player import Player


@dataclass
class Simulator:
    duration: int
    stake: int
    samples: int
    maxima: List[int]
    durations: List[int]
    player: Player
    game: Game
