import logging
from pathlib import Path


def configure_logging(level: int = logging.INFO) -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(
        level=level,
        format=fmt,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_dir / "trainer.log", encoding="utf-8"),
        ],
    )