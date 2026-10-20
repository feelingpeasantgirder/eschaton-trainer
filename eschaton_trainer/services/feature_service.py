import logging
import threading

from eschaton_trainer.core.memory_reader import MemoryReader
from eschaton_trainer.services.offset_service import OffsetService
from eschaton_trainer.models.player_state import PlayerState

log = logging.getLogger("eschaton.features")


class FeatureService:
    def __init__(self, reader: MemoryReader, offsets: OffsetService):
        self.reader = reader
        self.offsets = offsets
        self.state = PlayerState()
        self._stop = threading.Event()

    def _base(self) -> int:
        sig = self.offsets.get("player_base")
        if not sig:
            raise RuntimeError("player_base signature missing")
        return self.reader.resolve_pointer(sig["module_base"], sig["offsets"])

    def refresh(self) -> PlayerState:
        base = self._base()
        self.state.health = self.reader.read_float(base + 0x1A0)
        self.state.ammo = self.reader.read_int(base + 0x2C8)
        self.state.godmode = self.reader.read_bytes(base + 0x310, 1)[0] == 0x01
        return self.state

    def set_godmode(self, enabled: bool) -> None:
        base = self._base()
        self.reader.write_int(base + 0x310, 1 if enabled else 0)
        log.info("godmode -> %s", enabled)

    def refill_ammo(self, amount: int = 999) -> None:
        base = self._base()
        self.reader.write_int(base + 0x2C8, amount)
        log.info("ammo refilled to %d", amount)

    def start_headless(self) -> None:
        def _loop() -> None:
            while not self._stop.is_set():
                try:
                    self.refresh()
                except Exception as exc:  # noqa: BLE001
                    log.warning("refresh failed: %s", exc)
                self._stop.wait(0.5)

        threading.Thread(target=_loop, daemon=True, name="feature-loop").start()