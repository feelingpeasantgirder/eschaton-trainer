from eschaton_trainer.models.player_state import PlayerState


def test_health_pct_clamps():
    s = PlayerState(health=150.0, max_health=100.0)
    assert s.health_pct == 1.0


def test_health_pct_zero_max():
    s = PlayerState(health=50.0, max_health=0.0)
    assert s.health_pct == 0.0