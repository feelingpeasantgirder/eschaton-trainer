import logging
import time

from eschaton_trainer.bootstrap.process_finder import find_game_process
from eschaton_trainer.core.memory_reader import MemoryReader
from eschaton_trainer.services.offset_service import OffsetService
from eschaton_trainer.services.feature_service import FeatureService
from eschaton_trainer.overlay.hud import OverlayHud

log = logging.getLogger("eschaton.launcher")


class TrainerLauncher:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.offsets = OffsetService(config_path)
        self.reader: MemoryReader | None = None

    def run(self, dry_run: bool = False, overlay: bool = True) -> int:
        self.offsets.load()
        log.info("loaded %d signatures for build %s",
                 len(self.offsets.signatures), self.offsets.game_build)

        if dry_run:
            log.info("dry-run: skipping process attach")
            return 0

        proc = find_game_process("Eschaton.exe")
        if proc is None:
            log.error("Guns of Eschaton not running")
            return 2

        self.reader = MemoryReader(proc.pid)
        self.reader.attach()
        log.info("attached to pid=%d", proc.pid)

        features = FeatureService(self.reader, self.offsets)
        if overlay:
            OverlayHud(features).run()
        else:
            features.start_headless()
            while True:
                time.sleep(1.0)
        return 0