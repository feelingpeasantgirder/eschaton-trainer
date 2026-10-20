import json
import logging
from pathlib import Path

import yaml

log = logging.getLogger("eschaton.offsets")


class OffsetService:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.game_build: str = "unknown"
        self.signatures: dict[str, dict] = {}

    def load(self) -> None:
        if not self.config_path.exists():
            log.warning("config %s missing, using empty offset table", self.config_path)
            return
        with self.config_path.open("r", encoding="utf-8") as fh:
            cfg = yaml.safe_load(fh) or {}
        self.game_build = cfg.get("game_build", "unknown")
        self.signatures = cfg.get("signatures", {})
        log.debug("offset table loaded: %s", list(self.signatures))

    def get(self, name: str) -> dict | None:
        return self.signatures.get(name)

    def dump(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump({"build": self.game_build, "sigs": self.signatures}, fh, indent=2)