from dataclasses import dataclass, field


@dataclass
class PlayerState:
    health: float = 100.0
    max_health: float = 100.0
    ammo: int = 30
    reserve: int = 120
    godmode: bool = False
    infinite_ammo: bool = False
    active_buffs: list[str] = field(default_factory=list)

    @property
    def health_pct(self) -> float:
        if self.max_health <= 0:
            return 0.0
        return max(0.0, min(1.0, self.health / self.max_health))