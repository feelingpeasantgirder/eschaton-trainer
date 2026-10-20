"""Helper: dump current offset table to JSON for debugging."""

import sys

from eschaton_trainer.services.offset_service import OffsetService
from eschaton_trainer.utils.logging_setup import configure_logging


def main() -> int:
    configure_logging()
    svc = OffsetService("config/default.yaml")
    svc.load()
    out = sys.argv[1] if len(sys.argv) > 1 else "offsets_dump.json"
    svc.dump(out)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())