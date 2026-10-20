from eschaton_trainer.services.offset_service import OffsetService


def test_offset_service_loads_defaults():
    svc = OffsetService("config/default.yaml")
    svc.load()
    assert svc.game_build == "2026.03.1178"
    assert "player_base" in svc.signatures
    assert svc.get("player_base")["offsets"] == [0x0, 0x18, 0x2A0]


def test_missing_signature_returns_none():
    svc = OffsetService("config/default.yaml")
    svc.load()
    assert svc.get("does_not_exist") is None