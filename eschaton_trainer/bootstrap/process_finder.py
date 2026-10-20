import logging
from dataclasses import dataclass

import psutil

log = logging.getLogger("eschaton.proc")


@dataclass
class GameProcess:
    pid: int
    name: str
    exe: str


def find_game_process(exe_name: str) -> GameProcess | None:
    for p in psutil.process_iter(["pid", "name", "exe"]):
        try:
            if p.info["name"] and p.info["name"].lower() == exe_name.lower():
                return GameProcess(p.info["pid"], p.info["name"], p.info["exe"] or "")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None